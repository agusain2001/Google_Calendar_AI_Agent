# Google Calendar AI Agent

## Overview
Google Calendar AI Agent is a Flask-based API that leverages **Google Calendar API** and **Google Gemini API** to provide AI-powered event management. It enables users to create calendar events using natural language input, get daily event summaries, and categorize events automatically.

## Features
- **Natural Language Event Creation:** Converts user input into structured calendar events.
- **Automated Event Categorization:** Classifies events into categories and assigns priority.
- **Daily Summary & Smart Reminders:** Fetches daily events and sends reminders for upcoming events.
- **Google Calendar Integration:** Interacts with Google Calendar API for event management.
- **AI-powered NLP Processing:** Uses Google Gemini API for understanding and parsing user input.

---

## File Structure
```
google-calendar-ai-agent/
│
├── README.md
├── requirements.txt
├── app.py
├── agents/
│   ├── __init__.py
│   ├── event_creator.py
│   ├── reminder_summary.py
│   └── event_categorizer.py
├── utils/
│   ├── __init__.py
│   ├── calendar_client.py
│   ├── nlp_utils.py
│   └── notification_client.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── models/
│   ├── __init__.py
│   └── event_classifier.py
├── tests/
│   ├── __init__.py
│   ├── test_event_creator.py
│   ├── test_reminder_summary.py
│   └── test_event_categorizer.py
```

---

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### Step 1: Clone the Repository
```bash
git clone https://github.com/agusain2001/Google_Calendar_AI_Agent.git
cd google-calendar-ai-agent
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Environment Variables
```bash
export GOOGLE_CREDENTIALS_PATH="path/to/credentials.json"
export GEMINI_API_KEY="your-gemini-api-key"
export CALENDAR_ID="your-calendar-id"
```

### Step 4: Run the Flask Application
```bash
python app.py
```

---

## API Endpoints
### 1. Create Event
- **Endpoint:** `POST /create_event`
- **Description:** Converts natural language input into a structured Google Calendar event.
- **Request Body:**
```json
{
  "user_input": "Team meeting tomorrow at 2pm with alice@example.com and bob@example.com"
}
```
- **Response:**
```json
{
  "status": "success",
  "event": {
    "id": "event_id",
    "summary": "Team meeting",
    "start": "2024-02-11T14:00:00Z",
    "end": "2024-02-11T15:00:00Z"
  }
}
```
- **Curl Command:**
```bash
curl -X POST http://localhost:5000/create_event \
-H "Content-Type: application/json" \
-d '{"user_input": "Team meeting tomorrow at 2pm with alice@example.com and bob@example.com"}'
```

### 2. Get Daily Summary
- **Endpoint:** `GET /daily_summary`
- **Description:** Retrieves a summary of all scheduled events for the day, along with reminders for events happening soon.
- **Response:**
```json
{
  "date": "2024-02-11",
  "events": [
    {
      "title": "Morning Standup",
      "time": "2024-02-11T09:00:00Z",
      "attendees": ["team@example.com"]
    }
  ],
  "reminders": [
    "Reminder: Morning Standup at 09:00 AM"
  ]
}
```
- **Curl Command:**
```bash
curl http://localhost:5000/daily_summary
```

### 3. Categorize Events
- **Endpoint:** `GET /categorize_events`
- **Description:** Categorizes upcoming events using an AI model.
- **Response:**
```json
[
  {
    "event": "Client Meeting",
    "start_time": "2024-02-11T10:00:00Z",
    "category": "meeting",
    "priority": "high"
  }
]
```
- **Curl Command:**
```bash
curl http://localhost:5000/categorize_events
```

---

## Technology Stack
- **Backend:** Flask (Python)
- **NLP:** Google Gemini API
- **Calendar Integration:** Google Calendar API
- **Machine Learning:** Scikit-learn (for event categorization)
- **Storage:** Google Calendar (cloud-based event storage)

---

## Key Components
### 1. `agents/event_creator.py`
- Parses user input using NLP.
- Creates Google Calendar events via API.

### 2. `agents/reminder_summary.py`
- Fetches daily events.
- Sends reminders for upcoming events.

### 3. `agents/event_categorizer.py`
- Categorizes events using a Naive Bayes classifier.
- Assigns priority based on event type.

### 4. `utils/nlp_utils.py`
- Integrates **Google Gemini API** for NLP processing.
- Extracts event details from user input.

### 5. `utils/calendar_client.py`
- Handles interactions with Google Calendar API.

### 6. `models/event_classifier.py`
- Uses **TF-IDF** and **Naive Bayes** for event categorization.

---

## Testing
Run unit tests to verify functionality:
```bash
pytest tests/
```
---

## Future Enhancements
- Integrate **voice commands** for hands-free scheduling.
- Implement **user authentication** for multi-user support.
- Enhance **event categorization** using deep learning.

---
