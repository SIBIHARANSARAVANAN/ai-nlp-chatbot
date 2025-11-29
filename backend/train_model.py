
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training samples and labels
texts = [
    # greeting
    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening",
    "yo",
    "hi there",

    # goodbye
    "bye",
    "see you",
    "good night",
    "talk to you later",
    "bye bye",

    # thanks
    "thank you",
    "thanks",
    "thanks a lot",
    "appreciate it",

    # mood
    "how are you",
    "how is it going",
    "how are you doing",

    # help
    "can you help me",
    "i need some help",
    "please help",
    "i have a doubt",
    "i have a question",

    # ai_basics
    "what is ai",
    "explain artificial intelligence",
    "what is machine learning",
    "difference between ai and ml",
    "what should i learn to start ai",
    "ai basics",
    "how to start learning ai",

    # ai_roadmap
    "ai roadmap",
    "step by step roadmap for ai",
    "how to become an ai engineer",
    "roadmap to become data scientist",
    "what should i learn after python for ai",
    "tell me ai learning path",

    # ai_projects
    "ai project ideas",
    "give me some ai projects",
    "project ideas for machine learning",
    "final year ai project ideas",
    "projects for freshers in ai",

    # ai_interview
    "how to prepare for ai interview",
    "ai fresher interview questions",
    "what topics should i study for ml interview",
    "interview questions for data science fresher",
    "important topics for ai interview"
]

labels = [
    # greeting
    "greeting","greeting","greeting","greeting","greeting","greeting","greeting",
    # goodbye
    "goodbye","goodbye","goodbye","goodbye","goodbye",
    # thanks
    "thanks","thanks","thanks","thanks",
    # mood
    "mood","mood","mood",
    # help
    "help","help","help","help","help",
    # ai_basics
    "ai_basics","ai_basics","ai_basics","ai_basics","ai_basics","ai_basics","ai_basics",
    # ai_roadmap
    "ai_roadmap","ai_roadmap","ai_roadmap","ai_roadmap","ai_roadmap","ai_roadmap",
    # ai_projects
    "ai_projects","ai_projects","ai_projects","ai_projects","ai_projects",
    # ai_interview
    "ai_interview","ai_interview","ai_interview","ai_interview","ai_interview",
]

print("Training TF-IDF + Logistic Regression model...")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Training complete. model.pkl and vectorizer.pkl have been saved.")
