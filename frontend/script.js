const API_URL = "http://localhost:8000/chat";


 // change to Render URL after deploy

const messageInput = document.getElementById("messageInput");
const chatBox = document.getElementById("chat-box");
const typingIndicator = document.getElementById("typing");
const themeToggle = document.getElementById("themeToggle");
const emojiBtn = document.getElementById("emojiBtn");
const micButton = document.getElementById("micButton");
const sendBtn = document.getElementById("sendBtn");

const emojis = ["😀","😁","😂","🤣","😍","😎","🙏","🔥","👍","🤖","✨","💡","🚀"];

async function sendMessage() {
  const text = messageInput.value.trim();
  if (!text) return;
  console.log("Calling backend:", API_URL);

  addMessage(text, "user");
  messageInput.value = "";

  showTyping(true);

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    setTimeout(() => {
      showTyping(false);
      addMessage(data.reply || "No response from server.", "bot");
    }, 500);
  } catch (err) {
    console.error(err);
    showTyping(false);
    addMessage("Error: could not reach backend API.", "bot");
  }
}

function addMessage(message, type) {
  const bubble = document.createElement("div");
  bubble.className = `message ${type}`;

  const avatar = document.createElement("div");
  avatar.className = "avatar";

  const textEl = document.createElement("div");
  textEl.textContent = message;

  bubble.appendChild(avatar);
  bubble.appendChild(textEl);
  chatBox.appendChild(bubble);

  chatBox.scrollTop = chatBox.scrollHeight;

  // Save to localStorage
  const history = JSON.parse(localStorage.getItem("chatHistory") || "[]");
  history.push({ message, type });
  localStorage.setItem("chatHistory", JSON.stringify(history));
}

function loadHistory() {
  const history = JSON.parse(localStorage.getItem("chatHistory") || "[]");
  history.forEach(item => addMessage(item.message, item.type));
}

function showTyping(state) {
  if (state) {
    typingIndicator.classList.remove("hidden");
  } else {
    typingIndicator.classList.add("hidden");
  }
}

// Theme toggle
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

// Emoji picker
emojiBtn.addEventListener("click", () => {
  const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
  messageInput.value += randomEmoji;
  messageInput.focus();
});

// Voice input
let recognition = null;
if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SR();
  recognition.lang = "en-US";

  recognition.onresult = (event) => {
    const text = event.results[0][0].transcript;
    messageInput.value = text;
    micButton.textContent = "🎤";
  };

  recognition.onerror = () => {
    micButton.textContent = "🎤";
  };
}

micButton.addEventListener("click", () => {
  if (!recognition) {
    alert("Speech recognition is not supported in this browser.");
    return;
  }
  recognition.start();
  micButton.textContent = "🎙️";
});

// Send on button click or Enter
sendBtn.addEventListener("click", sendMessage);
messageInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

// Load old messages
window.addEventListener("load", () => {
  loadHistory();
  // Optional greeting
  if (!localStorage.getItem("hasGreeted")) {
    addMessage("Hi! I'm your AI NLP chatbot. Ask me about AI basics, roadmap, projects, or interview prep.", "bot");
    localStorage.setItem("hasGreeted", "true");
  }
});
