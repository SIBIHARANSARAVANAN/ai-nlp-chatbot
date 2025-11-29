
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="AI NLP Chatbot")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# Try to load model/vectorizer
model = None
vectorizer = None
if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "AI NLP Chatbot backend is running",
    }

@app.post("/chat")
def chat(data: Message):
    user_text = data.text.strip()

    # Fallback if model not loaded
    if model is None or vectorizer is None:
        return {
            "reply": "The NLP model is not trained yet. Please run train_model.py in the backend folder."
        }

    X = vectorizer.transform([user_text])
    intent = model.predict(X)[0]

    # Simple response logic based on predicted intent
    responses = {
        "greeting": "Hi there! I'm your AI assistant. How can I help you today?",
        "goodbye": "Goodbye! All the best for your AI journey 👋",
        "thanks": "You're welcome! Keep learning and exploring AI 🤖",
        "mood": "I'm just code, but I'm running perfectly! How are *you* feeling about AI?",
        "help": "Sure! Ask me about AI basics, roadmaps, projects, or interview prep.",
        "ai_basics": "AI (Artificial Intelligence) is about making machines think and act intelligently. You can start with Python, math (linear algebra & probability), and basic ML algorithms.",
        "ai_roadmap": "AI Roadmap for a fresher: 1) Python, 2) Math basics, 3) ML (regression, classification), 4) Deep Learning, 5) NLP/CV, 6) Projects + GitHub, 7) Internships / Jobs.",
        "ai_projects": "Some AI project ideas: spam classifier, movie recommender, chatbot, sentiment analysis, face recognition, or AI-powered resume analyzer.",
        "ai_interview": "For AI fresher interviews, focus on: ML algorithms, overfitting vs underfitting, train/test split, evaluation metrics, and at least 2–3 good projects you can explain clearly.",
    }

    reply = responses.get(intent, "Hmm, I’m not sure I understood that. Try asking about AI basics, roadmap, projects, or interviews.")
    return {"reply": reply}
