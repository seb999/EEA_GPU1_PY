import openai
import os
from dotenv import load_dotenv


# Load API key from .env file
load_dotenv()

API_KEY_GPU1 = os.getenv("API_KEY")

client = openai.OpenAI(
    api_key=API_KEY_GPU1,
    base_url="https://llmgw.eea.europa.eu/v1"
)

conversation = []

def stream_chat_with_model(prompt: str, model: str = "Inhouse-LLM/Mistral-Small-3.1-24B-Instruct-2503"):
    conversation.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        stream=True
    )

    full_reply = ""
    print("\nAssistant:", end=" ", flush=True)

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            full_reply += content

    print("\n")
    conversation.append({"role": "assistant", "content": full_reply})

if __name__ == "__main__":
    print("👋 Chatbot is running! Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        stream_chat_with_model(user_input)
