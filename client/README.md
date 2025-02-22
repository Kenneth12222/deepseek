# DeepSeek Chat Client

The **DeepSeek Chat Client** is a web-based front-end application designed to interact with the DeepSeek Chat API. It provides a user-friendly interface for sending and receiving messages from the DeepSeek chat model. The application features a responsive design, light/dark mode toggle, and smooth animations for an enhanced user experience.

## Features

- **Real-Time Chat Interaction**: Send messages to the DeepSeek Chat API and receive responses in real-time.
- **Light/Dark Mode Toggle**: Switch between light and dark themes with a single click. User preferences are saved in `localStorage`.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Smooth Animations**: Messages fade in smoothly for a polished user experience.
- **FontAwesome Icons**: Utilizes FontAwesome for theme toggle icons.

## Prerequisites

Before running the project, ensure you have the following:

- A modern web browser (e.g., Chrome, Firefox, Safari).
- Access to the DeepSeek Chat API (backend server running at `http://127.0.0.1:5000`).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kenneth12222/client_deep_seek.git
   cd client_deep_seek
   ```

2. **Run the Backend Server**:
   Ensure the DeepSeek Chat API backend is running. Follow the instructions in the [DeepSeek Chat API README](https://github.com/Kenneth12222/client_deep_seek.git) to set it up.

3. **Open the Client**:
   Open the `index.html` file in your browser:
   ```bash
   open index.html  # On macOS
   start index.html # On Windows
   ```

   Alternatively, you can serve the project using a local HTTP server:
   ```bash
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your browser.

## Usage

1. **Enter a Message**:
   - Type your message in the input box at the bottom of the chat window.
   - Press `Enter` or click the **Send** button to submit the message.

2. **Toggle Light/Dark Mode**:
   - Click the moon/sun icon in the top-right corner to switch between light and dark themes.

3. **View Responses**:
   - Messages from the user and the assistant will appear in the chat window.
   - The chat window automatically scrolls to show the latest message.

## Project Structure

- **`index.html`**: The main HTML file containing the structure of the chat interface.
- **`styles.css`**: Contains all the CSS styles for the application, including light/dark mode themes.
- **`script.js`**: Handles the chat functionality, including sending messages and displaying responses.
- **`logo.png`**: The logo displayed in the header.

## Customization

### Themes
The application supports light and dark modes. You can customize the colors by modifying the `:root` and `.light_mode` CSS variables in `styles.css`.

### API Endpoint
By default, the client sends requests to `http://127.0.0.1:5000/chat`. To change the API endpoint, update the `fetch` URL in `script.js`:
```javascript
fetch("http://your-api-endpoint/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: messageText })
})
```

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

- [FontAwesome](https://fontawesome.com/) for providing icons.
- [DeepSeek Chat API](https://github.com/Kenneth12222/client_deep_seek.git) for the backend integration.
- [OpenAI SDK](https://github.com/openai/openai-python) for interacting with the DeepSeek API.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/Kenneth12222/client_deep_seek.git).

---

Thank you for using the DeepSeek Chat Client! We hope it provides a seamless and enjoyable chat experience.