import sys
sys.path.append("src")
from gmail_client import authenticate_gmail, get_unread_emails, parse_email

service = authenticate_gmail()
print("✓ Authentifizierung erfolgreich")

emails = get_unread_emails(service, max_results=3)
print(f"✓ {len(emails)} ungelesene E-Mails gefunden")
for email in emails:
    parsed = parse_email(email)
    print(f"\n--- E-Mail ---")
    print(f"Von: {parsed['sender']}")
    print(f"Betreff: {parsed['subject']}")
    print(f"Body (erste 100 Zeichen): {parsed['body'][:100]}")