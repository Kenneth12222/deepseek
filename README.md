# DeepSeek Chat API

The DeepSeek Chat API is a Python-based Flask application that provides a simple interface to interact with the DeepSeek chat model using the OpenAI SDK. This project allows you to send user messages to the DeepSeek chat model and receive responses in real-time.

## Features

- **Chat Interaction**: Send user messages to the DeepSeek chat model and receive responses.
- **Environment Variable Configuration**: Securely manage API keys and server configurations using environment variables.
- **Robust Logging**: Comprehensive logging for error tracking and debugging.
- **RESTful API**: Exposes a RESTful API endpoint for chat interactions.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- `pip` (Python package manager)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kenneth12222/deepseek.git
   cd deepseek
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory of the project and add the following variables:
   ```plaintext
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   HOST=127.0.0.1  # Optional: Default is 127.0.0.1
   PORT=5000       # Optional: Default is 5000
   FLASK_DEBUG=true  # Optional: Set to "true" for debug mode
   ```

   Replace `your_deepseek_api_key_here` with your actual DeepSeek API key.

## Usage

1. **Run the Flask Application**:
   ```bash
   python app.py
   ```

   The server will start on the specified host and port (default: `127.0.0.1:5000`).

2. **Interact with the API**:
   - **Home Page**: Visit `http://127.0.0.1:5000/` to see the welcome message.
   - **Chat Endpoint**: Send a POST request to `http://127.0.0.1:5000/chat` with a JSON payload containing a `message` field.

   Example using `curl`:
   ```bash
   curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello, how are you?"}'
   ```

   Example Response:
   ```json
   {
       "response": "I'm just a computer program, so I don't have feelings, but I'm here to help you!"
   }
   ```

## API Endpoints

- **GET `/`**: Returns a welcome message.
- **POST `/chat`**: Accepts a JSON payload with a `message` field and returns the chat model's response.

## Configuration

The following environment variables can be configured:

- `DEEPSEEK_API_KEY`: Your DeepSeek API key (required).
- `HOST`: The host address to run the Flask server (default: `127.0.0.1`).
- `PORT`: The port to run the Flask server (default: `5000`).
- `FLASK_DEBUG`: Set to `true` to enable Flask debug mode (default: `false`).

## Logging

The application logs important events and errors to the console. Logs include:

- Server start and stop events.
- Invalid payload warnings.
- Successful chat interactions.
- Internal server errors.

## Error Handling

The API handles various errors gracefully:

- **Invalid Payload**: Returns a `400 Bad Request` with an error message.
- **Internal Server Error**: Returns a `500 Internal Server Error` with error details.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [OpenAI SDK](https://github.com/openai/openai-python) for interacting with the DeepSeek API.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/yourusername/deepseek-chat-api/issues).

---

Thank you for using the DeepSeek Chat API! We hope it serves your needs well.