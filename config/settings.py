from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

google_credentials = os.getenv("GOOGLE_CREDENTIALS_PATH")
gemini_api_key = os.getenv("GEMINI_API_KEY")
