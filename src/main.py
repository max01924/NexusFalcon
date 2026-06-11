import sys
sys.path.append("src")
from database import insert_email
from ai_analyzer import analyze_email
from gmail_client import parse_email

def process_and_save_email(analyzed_email, parsed_email):
    """
    Verarbeitet und speichert eine E-Mail.
    Args:
        analyzed_email: Analyzierte E-Mail-Daten
        parsed_email: Parsed E-Mail-Daten
    """

    combined_data = {
        "gmail_message_id": parsed_email["gmail_message_id"],
        "sender": parsed_email["sender"],
        "subject": parsed_email["subject"],
        "date_received": parsed_email["date_received"],
        "body_full": parsed_email["body_full"],
        "body_summary": "\n".join(analyzed_email["body_summary"]),
        "ai_tag_sentence": analyzed_email["ai_tag_sentence"]
    }
    
    inserted = insert_email(combined_data)
