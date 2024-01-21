import os
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

GOOGLE_API_TOKEN: str = os.getenv('GOOGLE_API_TOKEN')

llm = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_TOKEN,
    model="gemini-pro"
)
