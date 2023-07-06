import os

class Config:
    ENDPOINT = os.environ.get('ENDPOINT', 'http://127.0.0.1:20080') # aurora endpoint
    if 'https' in ENDPOINT:
        pass
    elif 'http' not in ENDPOINT:
        ENDPOINT = 'http://'+ ENDPOINT
    FLASK_PORT = os.environ.get('FLASK_PORT', 5000) # metrics port
