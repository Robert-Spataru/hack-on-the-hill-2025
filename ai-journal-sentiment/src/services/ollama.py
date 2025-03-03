import requests
import json

EXAMPLE_PROMPT = """Analyze this document, extracting all dates mentioned and the corresponding sentiment for each date.

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

def analyze_sentiment(prompt=EXAMPLE_PROMPT, model=MODEL, document=""):
    """
    Send a document to Ollama for sentiment analysis.
    
    Args:
        prompt (str): The prompt for Ollama to analyze the document
        model (str): The Ollama model identifier to use
        document (str): The text to analyze
    
    Returns:
        dict: Parsed JSON response containing sentiment analysis
    """
    url = "http://localhost:11434/api/generate"
    
    # Create the JSON structure for Ollama API
    payload = {
        "model": model,
        "prompt": f"{prompt}\n\nDocument: {document}",
        "stream": False,
        "format": "json",  # Request JSON output format
        "options": {
            "temperature": 0.6  # Low temperature for more deterministic output
        }
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        result = response.json()
        
        # Parse the JSON string from the response
        if 'response' in result:
            try:
                # The response might be a JSON string that needs parsing
                sentiment_data = json.loads(result['response'])
                return sentiment_data
            except json.JSONDecodeError:
                # If not parseable JSON, return the raw response
                return {"raw_response": result['response']}
        
        result = json.dumps(result, indent=2)
        return result
    except Exception as e:
        return {"error": str(e)}

def read_example_text(file_path):
    """
    Read the content of the example_text.txt file.
    
    Returns:
        str: The content of the file or an error message if file not found
    """
    try:
        # Adjust the path as needed to point to your text file
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Today was a challenging day but I learned a lot. I struggled with my project but finally had a breakthrough."
    except Exception as e:
        return f"Error reading file: {str(e)}"

    
# Example usage:
if __name__ == "__main__":
    example_document = read_example_text(file_path="/Users/robertspataru/Developer/hack-on-the-hill-2025/ai-journal-sentiment/src/services/example_text.txt")
    
    example_prompt = """Analyze this document, extracting all dates mentioned and the corresponding sentiment for each date.

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
    
    result = analyze_sentiment(example_prompt, "qwen2.5:1.5b", example_document)
    print(result)
