
# AI NLP Chatbot (Fresher-Friendly)

This project is an AI-focused NLP chatbot for freshers. It uses TF-IDF + Logistic Regression
to classify user messages into intents like greetings, AI basics, AI roadmap, AI projects,
and AI interview preparation.

## How to run backend locally

```bash
cd backend
pip install -r requirements.txt
python train_model.py
uvicorn main:app --reload
```

Backend runs at: http://127.0.0.1:8000

## Frontend

Open `frontend/index.html` in your browser (or serve with any static server).
Update the fetch URL in `script.js` when you deploy the backend to Render.
