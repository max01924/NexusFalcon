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
        self._window()
        self._email_list()
        self._email_details()

    def _position (self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def _window(self):
        self.paned = ttk.PanedWindow(self.root, orient="horizontal")
        self.paned.pack(fill="both", expand=True)
    
        self.frame_email_list = ttk.Frame(self.paned)
        self.frame_email_details = ttk.Frame(self.paned)

        self.paned.add(self.frame_email_list, weight=1)
        self.paned.add(self.frame_email_details, weight=2)

    def _email_list(self):
        self.treeview = ttk.Treeview(self.frame_email_list, columns=("sender", "subject", "date_received"), show="headings", selectmode="browse")

        self.treeview.heading("sender", text="Sender")
        self.treeview.heading("subject", text="Subject")
        self.treeview.heading("date_received", text="Date Received")

        self.treeview.column("sender", anchor="w")
        self.treeview.column("subject", anchor="w")
        self.treeview.column("date_received", anchor="w")

    def _email_details(self):
        self.label_sender = ttk.Label(
            self.frame_email_details,
            text=self.sender,
            wraplength=self.window_width - 20,
            font=("Helvetica", 10, "italic")
        )
        self.label_subject = ttk.Label(
            self.frame_email_details,
            text=self.subject,
            wraplength=self.window_width - 20,
            font=("Helvetica", 14, "normal")
        )
        self.label_date_received = ttk.Label(
            self.frame_email_details,
            text=self.date_received,
            wraplength=self.window_width - 20,
            font=("Helvetica", 10, "normal")
        )
        self.label_full_body = ttk.Label(
            self.frame_email_details,
            text=self.full_body,
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )
        self.label_ai_tag_sentence = ttk.Label(
            self.frame_email_details,
            text=self.ai_tag_sentence,
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )
        self.label_body_summary = ttk.Label(
            self.frame_email_details,
            text=self.body_summary,
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )
        
        self.label_sender.pack(fill="x", padx=10, pady=2)
        self.label_subject.pack(fill="x", padx=10, pady=2)
        self.label_date_received.pack(fill="x", padx=10, pady=2)
        self.label_full_body.pack(fill="x", padx=10, pady=2)
        self.label_ai_tag_sentence.pack(fill="x", padx=10, pady=2)
        self.label_body_summary.pack(fill="x", padx=10, pady=2)