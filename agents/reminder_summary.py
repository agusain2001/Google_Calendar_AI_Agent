from utils.calendar_client import GoogleCalendarClient
from utils.notification_client import NotificationClient
from datetime import datetime, timedelta

class ReminderSummary:
    def __init__(self):
        self.calendar = GoogleCalendarClient()
        self.notifier = NotificationClient()

    def generate_daily_summary(self):
        now = datetime.utcnow()
        end = now + timedelta(days=1)
        
        events = self.calendar.get_events(now.isoformat() + 'Z', end.isoformat() + 'Z')
        
        summary = {
            "date": now.date().isoformat(),
            "events": [],
            "reminders": []
        }
        
        for event in events:
            event_entry = {
                "title": event['summary'],
                "time": event['start']['dateTime'],
                "attendees": [a['email'] for a in event.get('attendees', [])]
            }
            summary['events'].append(event_entry)
            
            # Generate reminders for events starting in the next 2 hours
            start_time = datetime.fromisoformat(event['start']['dateTime'].replace('Z', '+00:00'))
            if (start_time - now) < timedelta(hours=2):
                reminder = f"Reminder: {event['summary']} at {event['start']['dateTime']}"
                self.notifier.send_reminder(reminder)
                summary['reminders'].append(reminder)
        
        return summary