const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");

sendButton.addEventListener("click", sendMessage);
messageInput.addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    const messageText = messageInput.value.trim();
    if (!messageText) return;
  
    addMessage("user", messageText);
    messageInput.value = "";
  
    // Use the correct absolute URL for your Flask server.
    fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: messageText })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      if (data.response) {
        addMessage("assistant", data.response);
      } else if (data.error) {
        addMessage("assistant", "Error: " + data.error);
      }
    })
    .catch(error => {
      console.error("Error:", error);
      addMessage("assistant", "An error occurred while sending your message: " + error.message);
    });
}
  
function addMessage(role, text) {
    const messageElem = document.createElement("div");
    messageElem.classList.add("message", role);
    messageElem.textContent = text;
    messagesDiv.appendChild(messageElem);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
