import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get('HOST')
FLASK_PORT = os.environ.get('FLASK_PORT')
FLASK_DEBUG = os.environ.get('FLASK_DEBUG')