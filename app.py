from flask import Flask, request, jsonify
from agents.event_creator import EventCreator
from agents.reminder_summary import ReminderSummary
from agents.event_categorizer import EventCategorizer

app = Flask(__name__)

# Initialize agents
event_creator = EventCreator()
reminder_summary = ReminderSummary()
event_categorizer = EventCategorizer()

@app.route('/create_event', methods=['POST'])
def handle_create_event():
    data = request.json
    try:
        event = event_creator.create_event_from_natural_language(data['user_input'])
        return jsonify({"status": "success", "event": event}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/daily_summary', methods=['GET'])
def handle_daily_summary():
    try:
        summary = reminder_summary.generate_daily_summary()
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/categorize_events', methods=['GET'])
def handle_categorize_events():
    try:
        categorized = event_categorizer.categorize_upcoming_events()
        return jsonify(categorized), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)