import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import GMAIL_SCOPES, GMAIL_CREDENTIALS_PATH, GMAIL_TOKEN_PATH


def authenticate_gmail():
    """
    Authentifiziert mit Gmail API via OAuth.
    Returns: Gmail API Service-Objekt
    """
    
    creds = None
    
    # Token laden falls vorhanden
    if os.path.exists(GMAIL_TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(GMAIL_TOKEN_PATH, GMAIL_SCOPES)
    
    # Token ungültig oder nicht vorhanden
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Token abgelaufen aber refresh möglich
            creds.refresh(Request())
        else:
            # Komplett neu authentifizieren
            flow = InstalledAppFlow.from_client_secrets_file(GMAIL_CREDENTIALS_PATH, GMAIL_SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Token speichern
        with open(GMAIL_TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    
    # Gmail Service erstellen
    service = build('gmail', 'v1', credentials=creds)
    return service


def get_unread_emails(service, max_results=10):
    """
    Holt ungelesene E-Mails.
    Args:
        service: Gmail API Service-Objekt
        max_results: Maximale Anzahl E-Mails
    Returns: Liste von E-Mail-Objekten
    """
    try:
        # Suche nach ungelesenen Mails
        results = service.users().messages().list(
            userId='me',
            q='is:unread',
            maxResults=max_results
        ).execute()
        
        messages = results.get('messages', [])
        
        if not messages:
            return []
        
        # Detaillierte Infos für jede Mail holen
        emails = []
        for msg in messages:
            email_data = service.users().messages().get(
                userId='me',
                id=msg['id'],
                format='full'
            ).execute()
            emails.append(email_data)
        
        return emails
    
    except Exception as e:
        print(f"Fehler beim Abrufen der E-Mails: {e}")
        return []


def parse_email(email_data):
    """
    Extrahiert relevante Daten aus Gmail API Response.
    Args:
        email_data: Rohe E-Mail-Daten von Gmail API
    Returns: Dict mit {message_id, sender, subject, date, body}
    """
    headers = email_data['payload']['headers']
    
    # Header-Daten extrahieren
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'Kein Betreff')
    sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unbekannt')
    date = next((h['value'] for h in headers if h['name'] == 'Date'), '')
    
    # Body extrahieren
    body = ''
    if 'parts' in email_data['payload']:
        for part in email_data['payload']['parts']:
            if part['mimeType'] == 'text/plain':
                body = part['body'].get('data', '')
                break
    else:
        body = email_data['payload']['body'].get('data', '')
    
    # Base64 decode
    if body:
        import base64
        body = base64.urlsafe_b64decode(body).decode('utf-8')
    
    return {
        'message_id': email_data['id'],
        'sender': sender,
        'subject': subject,
        'date': date,
        'body': body
    }