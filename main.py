from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

QUESTION_BANK = {
    "Java": [
        "Explain JVM architecture.",
        "What is the difference between JDK, JRE, and JVM?",
        "What are Java Streams?"
    ],
    "Python": [
        "What is the difference between a list and a tuple?",
        "Explain decorators in Python.",
        "What is a Python generator?"
    ],
    "C++": [
        "What is polymorphism in C++?",
        "What is the difference between stack and heap memory?",
        "Explain virtual functions."
    ]
}

class QuestionRequest(BaseModel):
    domain: str

@app.get("/")
def home():
    return {"message": "API Working"}

@app.post("/generate-question")
def generate_question(request: QuestionRequest):

    domain = request.domain.strip().title()

    if domain not in QUESTION_BANK:
        raise HTTPException(
            status_code=400,
            detail="Invalid domain"
        )

    return {
        "question": random.choice(QUESTION_BANK[domain])
    }