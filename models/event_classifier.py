from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

class EventClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()
        
        # Example training data (replace with real dataset)
        X_train = [
            "Team Meeting", 
            "Project Deadline",
            "Client Call",
            "Lunch Break",
            "Code Review"
        ]
        y_train = [
            "meeting", 
            "deadline", 
            "client", 
            "personal", 
            "development"
        ]
        
        X_vec = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_vec, y_train)
        
    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]