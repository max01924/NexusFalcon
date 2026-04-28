import sys
sys.path.append("src")
from database import create_table, insert_email, get_all_emails, get_email_by_id

#Table erstellen
create_table()
print("✓ Tabelle erstellt")

# Testemails
test_emails = [
    {
        "gmail_message_id": "test_001",
        "sender": "alice@example.com",
        "subject": "Test Mail 1",
        "date": "2024-01-01",
        "body": "Das ist eine Test-E-Mail"
    },

    {
        "gmail_message_id": "test_002",
        "sender": "max@example.com",
        "subject": "Test Mail 2",
        "date": "2024-01-01",
        "body": "Das ist eine Test-E-Mail"
    },

    {
        "gmail_message_id": "test_003",
        "sender": "rose@example.com",
        "subject": "Test Mail 3",
        "date": "2024-01-01",
        "body": "Das ist eine Test-E-Mail"
    }
]

# Emails einfügen
for email in test_emails:
    result = insert_email (email)
    print(f"✓ E-Mail eingefügt: {email['subject']} - {result}")

# Dublikat-Test
email = test_emails[0]
result = insert_email (email)
print(f"✓ E-Mail eingefügt: {email['subject']} - {result}")

# alle Mails ausgeben
emails = get_all_emails()
print(emails)
anzahl_emails = len(emails)
print(f"Anzahl an Emails: {anzahl_emails}")

#eine Email ausgeben
email = get_email_by_id(1)
print(email["subject"])