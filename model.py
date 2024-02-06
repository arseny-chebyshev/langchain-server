from langchain_google_genai import ChatGoogleGenerativeAI
from settings import GOOGLE_API_TOKEN

llm = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_TOKEN,
    model="gemini-pro"
)
