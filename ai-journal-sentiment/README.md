# README.md

# AI Journal Sentiment Analyzer

## Overview
The AI Journal Sentiment Analyzer is a Flask-based web application that allows users to submit journal entries and receive sentiment analysis results. The application utilizes the Ollama API for analyzing the text input and provides a user-friendly interface designed with Figma.

## Project Structure
```
ai-journal-sentiment
├── src
│   ├── api
│   ├── models
│   ├── services
│   ├── static
│   └── templates
├── tests
├── .env
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-journal-sentiment
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file.

## Usage
1. Run the application:
   ```
   python app.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

## Features
- Submit journal entries for sentiment analysis.
- View sentiment analysis results including score and label.
- Responsive design for a seamless user experience.

## Testing
To run the tests, use:
```
pytest tests/
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.