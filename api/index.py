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
        model="gpt-4o",
        instructions=(
            "You reply with ONLY raw markdown, no commentary or code fences, "
            "filling in this exact template (keep every line short):\n\n"
            "## \U0001F4A1 <project name>\n"
            "<one-sentence pitch>\n\n"
            "**Why not just use ChatGPT or existing tools?**\n"
            "<one sentence on what makes this hard to replicate with a "
            "generic chatbot or off-the-shelf product>\n\n"
            "**Key features:**\n"
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
