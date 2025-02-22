#!/usr/bin/env python3
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from openai import OpenAI

# Optional: Load environment variables from a .env file if available.
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Set up logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app.
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes.

# Retrieve the DeepSeek API key from environment variables.
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    logger.error("DEEPSEEK_API_KEY not found in environment variables. Please set it securely.")
    raise ValueError("DEEPSEEK_API_KEY not found in environment variables. Please set it securely.")

# Initialize the DeepSeek client.
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            logger.warning("Received invalid payload: %s", data)
            return jsonify({"error": "Missing 'message' field in JSON payload"}), 400

        user_message = data["message"]
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_message},
        ]

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )

        reply = response.choices[0].message.content
        logger.info("Chat request successful, reply: %s", reply)
        return jsonify({"response": reply})
    
    except Exception as e:
        logger.exception("Error processing chat request:")
        return jsonify({"error": "An internal error occurred", "details": str(e)}), 500

@app.route("/")
def index():
    return "Welcome to the DeepSeek Chat API. Use POST /chat to interact with the chat model."

def main():
    try:
        host = os.getenv("HOST", "127.0.0.1")
        port = int(os.getenv("PORT", 5000))
        debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
        
        logger.info("Starting Flask server on %s:%s with debug=%s", host, port, debug)
        app.run(host=host, port=port, debug=debug)
    except Exception as e:
        logger.exception("Error starting the Flask server:")
        raise

if __name__ == '__main__':
    main()
