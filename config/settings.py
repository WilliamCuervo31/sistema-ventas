import os
from dotenv import load_dotenv
import json

load_dotenv()

GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")
GOOGLE_SHEETS_WORKSHEET = os.getenv("GOOGLE_SHEETS_WORKSHEET")
GOOGLE_CREDENTIALS_JSON = json.loads(
    os.getenv("GOOGLE_CREDENTIALS_JSON")
)
APP_BASE_URL = os.getenv("APP_BASE_URL")
EMAIL_USER = os.getenv("EMAIL_USER")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")