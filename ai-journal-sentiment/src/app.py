from flask import Flask, render_template, request
from services.ollama import analyze_sentiment

PROMPT = """Analyze this document, extracting all dates mentioned and the corresponding sentiment for each date.

    Return ONLY a valid JSON object with this exact structure:
    {
    "data": [
        {
        "date": "YYYY-MM-DD",
        "sentiment_score": <float between -1.0 and 1.0>,
        "dominant_emotion": "<emotion word>",
        "confidence": <float between 0.0 and 1.0>
        },
        {
        "date": "YYYY-MM-DD",
        "sentiment_score": <float between -1.0 and 1.0>,
        "dominant_emotion": "<emotion word>",
        "confidence": <float between 0.0 and 1.0>
        }
    ]
    }

    Analysis rules:
    1. Find all specific dates mentioned in the text
    2. For each date, analyze the sentiment of events/experiences described for that specific date
    3. Convert all dates to YYYY-MM-DD format
    4. Use the full sentiment range from -1.0 (extremely negative) to 1.0 (extremely positive)
    5. Include only dates with associated events or experiences
    6. Return ONLY the JSON object with no additional text

    This format will enable direct time-series plotting of sentiment over dates.
    """

MODEL = "qwen2.5:1.5b"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Get text from the query parameters (for GET request)
    user_text = request.args.get('text_input')
    print(user_text)
    if user_text:
        # Analyze the text using analyze_sentiment
        analysis = analyze_sentiment(prompt="PROMPT", model="MODEL", docuemnt=user_text)
        # Render the result page with analysis
        return render_template('result.html', analysis=analysis)
    return render_template('journal.html')


if __name__ == '__main__':
    app.run(debug=True)
