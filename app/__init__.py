from flask import Flask
from app.extensions import mongo
from app.webhook.routes import webhook

def create_app():
    app = Flask(__name__)
    
    # Load configuration from .env file
    app.config.from_pyfile('../config.py')
    
    # Initialize extensions
    mongo.init_app(app)
    
    # Register blueprints
    app.register_blueprint(webhook)
    
    return app
