import os

import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

load_dotenv()

app = FastAPI()

# allow the Next.js dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET"],
)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

DATABASE_URL = os.environ["DATABASE_URL"]

# create the ideas table on startup if it doesn't exist yet
with psycopg.connect(DATABASE_URL) as conn:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS ideas (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )


@app.get("/api")
def get_idea():
    # ask the model for a project idea formatted to our markdown template
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=(
            "You reply with ONLY raw markdown, no commentary or code fences, "
            "filling in this exact template (keep every section short, 1-2 sentences):\n\n"
            "## \U0001F4A1 <project name>\n"
            "### The idea\n"
            "<what it is and what problem it solves>\n\n"
            "### \U0001F500 What's unique vs. ChatGPT\n"
            "<why a generic chatbot or off-the-shelf tool can't replicate this>\n\n"
            "### \U0001F4B0 Real value add\n"
            "<the concrete benefit that makes this worth building/paying for>\n"
            "- \U0001F527 <feature one, a few words>\n"
            "- \U0001F510 <feature two, a few words>\n"
            "- \U0001F680 <feature three, a few words>\n\n"
            "Never add headings, sections, or text beyond this template."
        ),
        input=(
            "Suggest one project idea at the intersection of cloud, "
            "security, and AI that could be monetized or gain popularity "
            "if someone spent time developing it."
        ),
    )
    idea = response.output_text

    # persist every generated idea so we can show past ideas later
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("INSERT INTO ideas (content) VALUES (%s)", (idea,))

    return {"idea": idea}


@app.get("/api/ideas")
def list_ideas():
    # return past ideas, most recent first
    with psycopg.connect(DATABASE_URL) as conn:
        rows = conn.execute(
            "SELECT id, content, created_at FROM ideas ORDER BY created_at DESC"
        ).fetchall()

    return {
        "ideas": [
            {"id": row[0], "content": row[1], "created_at": row[2].isoformat()}
            for row in rows
        ]
    }
