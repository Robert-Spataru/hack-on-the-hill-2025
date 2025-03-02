import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']
    TESTING = os.environ.get('TESTING', 'False').lower() in ['true', '1', 't']
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    OLLAMA_API_URL = os.environ.get('OLLAMA_API_URL')
    OLLAMA_API_KEY = os.environ.get('OLLAMA_API_KEY')