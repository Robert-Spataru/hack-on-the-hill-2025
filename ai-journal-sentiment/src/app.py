from flask import Flask, render_template, request
from services.ollama import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Get text from the query parameters (for GET request)
    user_text = request.args.get('text_input')
    print(user_text)
    if user_text:
        # Analyze the text using analyze_sentiment
        print("here")
        analysis = analyze_sentiment(user_text)
        # Render the result page with analysis
        return render_template('result.html', analysis=analysis)
    # If no text_input, show the input form
    print("here2")
    return render_template('journal.html')


if __name__ == '__main__':
    app.run(debug=True)
