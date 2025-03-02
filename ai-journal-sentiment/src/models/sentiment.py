class Sentiment:
    def __init__(self, score: float, label: str):
        self.score = score
        self.label = label
    
    def to_json(self):
        return {
            'score': self.score,
            'label': self.label
        }
    
    
    
    def __str__(self):
        return f"Sentiment(score={self.score}, label='{self.label}')"

    def __repr__(self):
        return f"Sentiment(score={self.score}, label='{self.label}')"