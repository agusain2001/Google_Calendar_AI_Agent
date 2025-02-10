from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import settings
import datetime

class GoogleCalendarClient:
    def __init__(self):
        self.service = build(
            'calendar', 
            'v3',
            credentials=service_account.Credentials.from_service_account_file(
                settings.GOOGLE_CREDENTIALS_PATH,
                scopes=['https://www.googleapis.com/auth/calendar']
            )
        )
        
    def create_event(self, event_body):
        return self.service.events().insert(
            calendarId=settings.CALENDAR_ID,
            body=event_body
        ).execute()
        
    def get_events(self, time_min, time_max):
        return self.service.events().list(
            calendarId=settings.CALENDAR_ID,
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy='startTime'
        ).execute().get('items', [])
        
    def get_upcoming_events(self, max_results=10):
        now = datetime.utcnow().isoformat() + 'Z'
        return self.service.events().list(
            calendarId=settings.CALENDAR_ID,
            timeMin=now,
            maxResults=max_results,
            singleEvents=True,
            orderBy='startTime'
        ).execute().get('items', [])