import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Gmail API
GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
GMAIL_CREDENTIALS_PATH = os.path.join(BASE_DIR, "config", "credentials.json")
GMAIL_TOKEN_PATH = os.path.join(BASE_DIR, "data", "token.json")
MAX_EMAILS_PER_FETCH = 10

#OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_MAX_TOKENS = 500

#Polling
POLLING_INTERVALL_SECONDS = 300

#Database
DATABASE_PATH = os.path.join(BASE_DIR, "/data", "mail_ai.db")

#Logging
LOG_FILE_PATH = os.path.join(BASE_DIR, "/logs", "app.log")
LOG_LEVEL = "INFO"

#Notification
NOTIFICATIONS_ENABLED = True