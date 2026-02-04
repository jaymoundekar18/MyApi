from fastapi import FastAPI
from textblob import TextBlob
import uvicorn
import re
# from mangum import Mangum

app = FastAPI(title="Sentiment Analysis API")

@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running"}

@app.get("/analyze/{text}")
def analyze_text(text: str):
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Determining sentiment of text
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Confidence based on polarity
    if abs(polarity) > 0.6:
        confidence = "High"
    elif abs(polarity) > 0.3:
        confidence = "Medium"
    else:
        confidence = "Low"

    # Subjectivity categorization
    if subjectivity <= 0.3:
        subjectivity_label = "Objective"
    elif subjectivity <= 0.6:
        subjectivity_label = "Mixed"
    else:
        subjectivity_label = "Subjective"

    # Text metrics
    words = text.split()
    char_count = len(text)
    # sentence_count = len(blob.sentences)
    sentence_count = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    lexical_diversity = len(set(words)) / len(words) if words else 0

    return {
        "text": text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "subjectivity_label": subjectivity_label,
        "sentiment": sentiment,
        "confidence": confidence,
        "word_count": len(words),
        "char_count": char_count,
        "sentence_count": sentence_count,
        "avg_word_length": avg_word_length,
        "lexical_diversity": lexical_diversity
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# handler = Mangum(app)
