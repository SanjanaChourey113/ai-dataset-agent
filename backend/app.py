import requests

# 1. Dataset read karna
import pandas as pd

def load_dataset():
    df = pd.read_csv("dataset/StudentsPerformance.csv")
    return df.to_string()


# 2. Ollama (Gemma) ko call karna
def ask_gemma(question):
    dataset_context = load_dataset()

    prompt = f"""
You are an AI assistant.
Use the following dataset to answer the question.

DATASET:
{dataset_context}

QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

