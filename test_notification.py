import sys
import tkinter as tk
sys.path.append("src")
from gmail_client import authenticate_gmail, get_unread_emails, parse_email
from ai_analyzer import analyze_email
from main import process_and_save_email
from notification import NotificationPopup
# gmail_client: sender, subject
# ai_analyzer: ai_tag_sentence, body_summary

root = tk.Tk()
root.withdraw()  # Hauptfenster ausblenden, für macOS bugfix

# Gmail authentifizieren
service = authenticate_gmail()

# Ungelesene Mails holen
emails = get_unread_emails(service, max_results=2)
print(f"{len(emails)} ungelesene Mails gefunden")

# Pipeline für jede Mail
for email_data in emails:
    parsed = parse_email(email_data)
    analyzed = analyze_email(parsed["body_full"])
    process_and_save_email(analyzed, parsed)
    print(f"Gespeichert: {parsed['subject']}")
    # Pop-up Benachrichtigungen für jede Mail anzeigen
    NotificationPopup(root, sender=parsed["sender"], subject=parsed["subject"], ai_tag_sentence=analyzed["ai_tag_sentence"], body_summary=analyzed["body_summary"])