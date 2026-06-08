import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET"],
)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@app.get("/api")
def get_idea():
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
    return {"idea": response.output_text}
