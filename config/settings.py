import os
from dotenv import load_dotenv
import json

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")
GOOGLE_SHEETS_WORKSHEET = os.getenv("GOOGLE_SHEETS_WORKSHEET")
GOOGLE_CREDENTIALS_JSON = json.loads(
    os.getenv("GOOGLE_CREDENTIALS_JSON")
)
APP_BASE_URL = os.getenv("APP_BASE_URL")