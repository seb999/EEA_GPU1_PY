import openai
import os
from dotenv import load_dotenv

# Load AP key from .env file
load_dotenv()

API_KEY_GPU1 = os.getenv("API_KEY")

client = openai.OpenAI(
    api_key=API_KEY_GPU1,
    base_url="https://llmgw.eea.europa.eu/v1" 
)

def stream_chat_completion(prompt: str, model: str = "Inhouse-LLM/Mistral-Small-3.1-24B-Instruct-2503") -> None:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in response:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)


if __name__ == "__main__":
    stream_chat_completion("this is a test request, who was Napoleon Bonaparte")
