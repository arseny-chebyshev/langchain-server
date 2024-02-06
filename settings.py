import os
from dotenv import load_dotenv


GOOGLE_API_TOKEN: str = os.getenv('GOOGLE_API_TOKEN')
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')