from flask import Blueprint, request, jsonify
from services.journal import save_journal_entry, get_journal_entries
from services.ollama import analyze_sentiment

api = Blueprint('api', __name__)

@api.route('/journal', methods=['POST'])
def submit_journal_entry():
    data = request.json
    entry = data.get('entry')
    if not entry:
        return jsonify({'error': 'Entry is required'}), 400
    
    save_journal_entry(entry)
    sentiment_result = analyze_sentiment(entry)
    
    return jsonify(sentiment_result), 201

@api.route('/journal', methods=['GET'])
def retrieve_journal_entries():
    entries = get_journal_entries()
    return jsonify(entries), 200