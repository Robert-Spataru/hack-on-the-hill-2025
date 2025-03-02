from typing import List, Dict, Any
from datetime import datetime

class Sentiment:
    def __init__(self, date: str, sentiment_score: float, dominant_emotion: str, confidence: float):
        self.date = date
        self.sentiment_score = sentiment_score
        self.dominant_emotion = dominant_emotion
        self.confidence = confidence
    
    def to_json(self):
        return {
            'date': self.date,
            'sentiment_score': self.sentiment_score,
            'dominant_emotion': self.dominant_emotion,
            'confidence': self.confidence
        }
    
    def __str__(self):
        return f"Sentiment(date='{self.date}', sentiment_score={self.sentiment_score}, dominant_emotion='{self.dominant_emotion}', confidence={self.confidence})"

    def __repr__(self):
        return self.__str__()


class SentimentAnalysis:
    def __init__(self, sentiments: List[Sentiment] = None):
        self.sentiments = sentiments or []
    
    @classmethod
    def from_json(cls, json_data: Dict[str, Any]):
        """Create a SentimentAnalysis object from JSON data"""
        sentiments = []
        if 'data' in json_data:
            for sentiment_data in json_data['data']:
                sentiment = Sentiment(
                    date=sentiment_data.get('date'),
                    sentiment_score=sentiment_data.get('sentiment_score'),
                    dominant_emotion=sentiment_data.get('dominant_emotion'),
                    confidence=sentiment_data.get('confidence')
                )
                sentiments.append(sentiment)
        return cls(sentiments)
    
    def to_json(self):
        return {
            'data': [sentiment.to_json() for sentiment in self.sentiments]
        }
    
    def add_sentiment(self, sentiment: Sentiment):
        self.sentiments.append(sentiment)
    
    def get_sentiments_by_date_range(self, start_date: str, end_date: str) -> List[Sentiment]:
        """Filter sentiments by date range"""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        return [
            sentiment for sentiment in self.sentiments 
            if start <= datetime.strptime(sentiment.date, "%Y-%m-%d") <= end
        ]
    
    def get_average_sentiment_score(self) -> float:
        """Calculate average sentiment score across all sentiments"""
        if not self.sentiments:
            return 0.0
        return sum(sentiment.sentiment_score for sentiment in self.sentiments) / len(self.sentiments)
    
    def __str__(self):
        return f"SentimentAnalysis(sentiments={len(self.sentiments)})"

    def __repr__(self):
        return self.__str__()