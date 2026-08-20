import tkinter as tk
from tkinter import ttk
import sqlite3
from database import get_all_emails

class EmailGui():

    def __init__(self, master, db_path):
        self.master = master
        self.db_path = db_path
        self.current_email_id = None

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
        x = (screen_width - self.window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{self.window_width}x{window_height}+{x}+{y}")

    def _window(self):
        self.paned = ttk.PanedWindow(self.root, orient="horizontal")
        self.paned.pack(fill="both", expand=True)
    
        self.frame_email_list = ttk.Frame(self.paned)
        self.frame_email_details = ttk.Frame(self.paned)

        self.paned.add(self.frame_email_list, weight=1)
        self.paned.add(self.frame_email_details, weight=2)

    def _email_list(self):
        self.emails = get_all_emails()

        self.treeview = ttk.Treeview(self.frame_email_list, columns=("sender", "subject", "date_received"), show="headings", selectmode="browse")

        self.treeview.heading("sender", text=f"{self.emails["sender"]}")
        self.treeview.heading("subject", text=f"{self.emails["subject"]}")
        self.treeview.heading("date_received", text="self.emails["date_received"]")

        self.treeview.column("sender", anchor="w")
        self.treeview.column("subject", anchor="w")
        self.treeview.column("date_received", anchor="w")

    def _email_details(self):
        self.label_sender.config(
            text=self.email["sender"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 10, "italic")
        )
        self.label_subject.config(
            self.frame_email_details,
            text=self.email["subject"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 14, "normal")
        )
        self.label_date_received.config(
            self.frame_email_details,
            text=self.email["date_received"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 10, "normal")
        )
        self.label_full_body.config(
            self.frame_email_details,
            text=self.email["full_body"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )
        self.label_ai_tag_sentence.config(
            self.frame_email_details,
            text=self.email["ai_tag_sentence"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )
        self.label_body_summary.config(
            self.frame_email_details,
            text=self.email["body_summary"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )