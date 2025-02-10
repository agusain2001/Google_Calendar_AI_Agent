from utils.calendar_client import GoogleCalendarClient
from models.event_classifier import EventClassifier

class EventCategorizer:
    def __init__(self):
        self.calendar = GoogleCalendarClient()
        self.classifier = EventClassifier()
        
    def categorize_upcoming_events(self):
        events = self.calendar.get_upcoming_events()
        categorized = []
        
        for event in events:
            category = self.classifier.predict(event['summary'])
            categorized.append({
                "event": event['summary'],
                "start_time": event['start']['dateTime'],
                "category": category,
                "priority": "high" if "meeting" in category.lower() else "normal"
            })
            
        return categorized