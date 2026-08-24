import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import DATABASE_PATH
import sqlite3

def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gmail_message_id TEXT UNIQUE NOT NULL,
            sender TEXT,
            subject TEXT,
            date_received TEXT,
            body_full TEXT,
            body_summary TEXT,
            ai_tag_sentence TEXT,
            is_read INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            replied_at TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_email(email_data):
    gmail_message_id = email_data ["gmail_message_id"]
    
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM emails WHERE gmail_message_id = ?", (gmail_message_id,))
    exists = cursor.fetchone()
    
    if exists:
        conn.close()  
        return False
    
    else:
        cursor.execute("""
            INSERT INTO emails (gmail_message_id, sender, subject, date_received, body_full, body_summary, ai_tag_sentence, is_read)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)               
        """, (
            email_data["gmail_message_id"],
            email_data["sender"],
            email_data["subject"],
            email_data["date_received"],
            email_data["body_full"],
            email_data["body_summary"],
            email_data["ai_tag_sentence"],
            0  # is_read = False
        ))
        conn.commit()
        conn.close()
        return True
    
def get_all_emails():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM emails ORDER BY created_at DESC")
    rows = cursor.fetchall()

    columns = [description[0] for description in cursor.description]
    results = [dict(zip(columns, row)) for row in rows]
    
    conn.close()
    return results

def get_email_by_id(email_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM emails WHERE id = ?", (email_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        columns = [description[0] for description in cursor.description]
        return dict(zip(columns, row))
    return None

def update_email_summary(email_id, summary, ai_tag):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE emails SET body_summary = ?, ai_tag_sentence = ? WHERE id = ?", (summary, ai_tag, email_id,))

    conn.commit()
    conn.close()    