from flask import Flask, request, Response
from flask_cors import CORS
import openai
import os
import json
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app) 

API_KEY_GPU1 = os.getenv("API_KEY")

client = openai.OpenAI(
    api_key=API_KEY_GPU1,
    base_url="https://llmgw.eea.europa.eu/v1"  
)

def generate_stream(messages: list, model: str = "Inhouse-LLM/Mistral-Small-3.1-24B-Instruct-2503"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            data = {"role": "assistant", "content": content}
            yield f"data: {json.dumps(data)}\n\n"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    model = data.get("model", "Inhouse-LLM/Mistral-Small-3.1-24B-Instruct-2503")

    if not prompt:
        return {"error": "Missing 'prompt' in request"}, 400

    return Response(generate_stream(prompt, model), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
