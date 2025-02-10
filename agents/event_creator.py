from utils.nlp_utils import parse_natural_language
from utils.calendar_client import GoogleCalendarClient

class EventCreator:
    def __init__(self):
        self.calendar = GoogleCalendarClient()
        
    def create_event_from_natural_language(self, user_input):
        event_details = parse_natural_language(user_input)
        created_event = self.calendar.create_event(event_details)
        return {
            "id": created_event['id'],
            "summary": created_event['summary'],
            "start": created_event['start']['dateTime'],
            "end": created_event['end']['dateTime']
        }