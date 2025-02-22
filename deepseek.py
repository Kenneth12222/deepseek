#!/usr/bin/env python3
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI, APIStatusError
from dotenv import load_dotenv

# Load environment variables from a .env file if available.
load_dotenv()

# Set up logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Centralized configuration class.
class Config:
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    if not DEEPSEEK_API_KEY:
        logger.error("DEEPSEEK_API_KEY not found in environment variables. Please set it securely.")
        raise ValueError("DEEPSEEK_API_KEY not found in environment variables. Please set it securely.")

# Initialize Flask app.
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes.

# Initialize the DeepSeek client.
client = OpenAI(api_key=Config.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

@app.route("/health", methods=["GET"])
def health():
    """Simple health-check endpoint."""
    return jsonify({"status": "ok"}), 200

@app.route("/chat", methods=["POST"])
def chat():
    """Endpoint to handle chat requests."""
    try:
        # Force JSON parsing even if the content type is missing.
        data = request.get_json(force=True)
        if not data or "message" not in data:
            logger.warning("Invalid payload received: %s", data)
            return jsonify({"error": "Missing 'message' field in JSON payload"}), 400

        user_message = data["message"]
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_message},
        ]

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )
        except APIStatusError as api_err:
            error_details = api_err.args[0] if api_err.args else str(api_err)
            logger.exception("API error during chat completion: %s", error_details)
            if "Insufficient Balance" in error_details:
                return jsonify({"error": "Insufficient account balance. Please top up your account."}), 402
            else:
                return jsonify({"error": "API error occurred", "details": error_details}), 500

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
        logger.info("Starting Flask server on %s:%s with debug=%s", Config.HOST, Config.PORT, Config.DEBUG)
        app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
    except Exception as e:
        logger.exception("Error starting the Flask server:")
        raise

if __name__ == '__main__':
    main()
