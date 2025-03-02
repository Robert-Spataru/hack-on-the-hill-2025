from flask import Flask
from src.api.routes import api_bp

app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')

# Register API blueprint
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
    
