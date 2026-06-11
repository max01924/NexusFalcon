import os
import sys
import json
from groq import Groq

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import GROQ_API_KEY, GROQ_MODEL, GROQ_MAX_TOKENS

_SYSTEM_PROMPT = """Du fasst E-Mails zusammen. Antworte ausschließlich mit gültigem JSON (kein Markdown, keine Codefences).
Das JSON muss genau diese Struktur haben:
{"summary": ["Stichpunkt 1", "Stichpunkt 2", ...], "one_sentence": "ein einzelner deutscher Satz"}
Für "summary": 3 bis 7 kurze sachliche Stichpunkte zum Inhalt.
Für "one_sentence": eine prägnante Gesamtzusammenfassung auf Deutsch."""

_USER_TEMPLATE = """Analysiere den folgenden E-Mail-Text:\n\n{body}"""


def analyze_email(email_body):
    """
    Analysiert E-Mail-Inhalt via Groq API.
    Args:
        email_body: E-Mail-Text
    Returns: Dict mit {"summary": [...], "one_sentence": "..."}
    """
    if not (email_body or "").strip():
        return {
            "summary": [],
            "one_sentence": "Kein E-Mail-Inhalt vorhanden.",
        }
    
    client = Groq(
        api_key=GROQ_API_KEY,
    )
    
    # Responses API nutzen
    response = client.chat.completions.create(
    model=GROQ_MODEL,
    messages=[
        {"role": "system", "content": _SYSTEM_PROMPT},
        {"role": "user", "content": _USER_TEMPLATE.format(body=email_body.strip())}
    ],
    response_format={"type": "json_object"},
    max_completion_tokens=GROQ_MAX_TOKENS,
    temperature=0.3
    )

    raw = response.choices[0].message.content
    
    if response.choices[0].finish_reason == "length":
        raise ValueError("Antwort wurde wegen Token-Limit abgeschnitten.")

    if not raw:
        raise ValueError("Leere Antwort von OpenAI.")
    
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ungültiges JSON in der Antwort: {e}") from e
    
    body_summary = data.get("summary")
    ai_tag_sentence = data.get("one_sentence")
    
    if not isinstance(body_summary, list):
        raise ValueError('"body_summary" muss eine Liste sein.')
    
    body_summary = [str(item) for item in body_summary]
    
    if not isinstance(ai_tag_sentence, str):
        raise ValueError('"ai_tag_sentence" muss ein String sein.')
    
    return {"body_summary": body_summary, "ai_tag_sentence": ai_tag_sentence}