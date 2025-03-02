import unittest
from src.models.sentiment import Sentiment
from src.services.journal import save_journal_entry
from src.services.ollama import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_sentiment_analysis_positive(self):
        entry = "I had a wonderful day!"
        result = analyze_sentiment(entry)
        self.assertIsInstance(result, Sentiment)
        self.assertGreater(result.score, 0)
        self.assertEqual(result.label, "positive")

    def test_sentiment_analysis_negative(self):
        entry = "I am feeling very sad."
        result = analyze_sentiment(entry)
        self.assertIsInstance(result, Sentiment)
        self.assertLess(result.score, 0)
        self.assertEqual(result.label, "negative")

    def test_save_journal_entry(self):
        entry = "Today was a great day!"
        save_journal_entry(entry)
        # Here you would typically check if the entry was saved correctly
        # This is a placeholder for the actual implementation

if __name__ == '__main__':
    unittest.main()