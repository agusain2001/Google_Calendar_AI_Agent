import google.generativeai as genai
from config import settings
from dateutil import parser

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def parse_natural_language(user_input):
    prompt = f"""
    Extract calendar event details from this input: "{user_input}"
    Return JSON format with:
    - summary (event title)
    - start_time (ISO 8601 format)
    - end_time (ISO 8601 format)
    - attendees (list of emails)
    - description (optional)
    """
    
    response = model.generate_content(prompt)
    
    try:
        event_data = eval(response.text)
        return {
            "summary": event_data.get('summary', 'Meeting'),
            "start": {"dateTime": parser.parse(event_data['start_time']).isoformat()},
            "end": {"dateTime": parser.parse(event_data['end_time']).isoformat()},
            "attendees": [{"email": email} for email in event_data.get('attendees', [])],
            "description": event_data.get('description', '')
        }
    except Exception as e:
        raise ValueError(f"Failed to parse event details: {str(e)}")