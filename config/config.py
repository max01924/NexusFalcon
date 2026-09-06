import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Gmail API
GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
GMAIL_CREDENTIALS_PATH = os.path.join(BASE_DIR, "config", "credentials.json")
GMAIL_TOKEN_PATH = os.path.join(BASE_DIR, "data", "token.json")
MAX_EMAILS_PER_FETCH = 10

#Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "openai/gpt-oss-20b"
GROQ_MAX_TOKENS_OUTPUT = 1000
GROQ_MAX_ZEICHEN_INPUT = 6000

#Polling
POLLING_INTERVALL_SECONDS = 300

#Database
DATABASE_PATH = os.path.join(BASE_DIR, "data", "database.db")

#Logging
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "app.log")
LOG_LEVEL = "INFO"

#Notification
NOTIFICATIONS_ENABLED = True