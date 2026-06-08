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
        model="gpt-5",
        input=(
            "Suggest one project idea at the intersection of cloud, security, "
            "and AI that could be monetized or gain popularity if someone "
            "spent time developing it. Refine the idea with enough detail to "
            "be actionable. Respond in markdown."
        ),
    )
    return {"idea": response.output_text}
