import tkinter as tk
from tkinter import ttk

class EmailGui():

    def __init__(self, master, sender, subject, body_full, date_received, ai_tag_sentence, body_summary):
        self.master = master
        self.sender = sender
        self.subject = subject
        self.body_full = body_full
        self.date_received = date_received
        self.ai_tag_sentence = ai_tag_sentence
        self.body_summary = body_summary

        self.root = tk.Toplevel(master)
        self.root.title("Email Inbox")
        self._position()

    def _position (self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def _frames (self)