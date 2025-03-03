import os

class Config:
    # Basic Flask configuration
    SECRET_KEY = 'your_secret_key'  # Change this in production
    
    # Email configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "y7hamzakhanswati@gmail.com"
    MAIL_PASSWORD = "sbep muwk dinz xsgx"
    MAIL_DEFAULT_SENDER = "y7hamzakhanswati@gmail.com"
    
    # Upload configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', 'uploads')
    
    # Database configuration
    DATABASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance', 'chatbot.db') 