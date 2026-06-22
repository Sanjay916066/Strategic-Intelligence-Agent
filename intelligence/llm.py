import ollama
from config import OLLAMA_MODEL


def generate(prompt):

    print(f"Using model: {OLLAMA_MODEL}")
    print("Calling Ollama...")

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 150
        }
    )

    print("Ollama finished.")

    return response["message"]["content"]