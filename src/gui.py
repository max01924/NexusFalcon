import tkinter as tk
from tkinter import ttk
from database import get_all_emails

class EmailGui():

    def __init__(self, master, db_path):
        self.master = master
        self.db_path = db_path
        self._refresh_emails()
        self.current_email_id = None

        self.root = tk.Toplevel(master)
        self.root.title("Email Inbox")
        self._position()
        self._window()
        self._email_list()

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
        self.treeview = ttk.Treeview(self.frame_email_list, columns=("sender", "subject", "date_received"), show="headings", selectmode="browse")

        if self.all_emails:

            for email in self.all_emails:
                self.treeview.heading("sender", text="Absender")
                self.treeview.heading("subject", text="Betreff")
                self.treeview.heading("date_received", text="Datum")

                self.treeview.insert("", "end", iid=email["id"], values=(email["sender"], email["subject"], email["date_received"]))

        else:
            self.treeview.heading("sender", text="Keine E-Mails gefunden")
            self.treeview.heading("subject", text="")
            self.treeview.heading("date_received", text="")

        self.treeview.pack(fill="both", expand=True)

        self.treeview.bind("<<TreeviewSelect>>", self._on_email_select)

        self._refresh_emails()

    def _on_email_select(self, event):
        selected = self.treeview.selection()
        if not selected:
            return
        self.current_email_id = int(selected[0])
        self._email_details(self.current_email_id)

    def _email_details(self, email_id):
        email = self.all_emails[email_id]

        self.label_sender.config(
            text=email["sender"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 10, "italic")
        )
        self.label_subject.config(
            text=email["subject"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 14, "normal")
        )
        self.label_date_received.config(
            text=email["date_received"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 10, "normal")
        )
        self.label_body_full.config(
            text=email["body_full"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )   
        self.label_ai_tag_sentence.config(
            text=email["ai_tag_sentence"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )
        self.label_body_summary.config(
            text=email["body_summary"],
            wraplength=self.window_width - 20,
            font=("Helvetica", 15, "normal")
        )

        self.label_sender.pack(fill="x", padx=10, pady=2)
        self.label_subject.pack(fill="x", padx=10, pady=2)
        self.label_date_received.pack(fill="x", padx=10, pady=2)
        self.label_body_full.pack(fill="x", padx=10, pady=2)
        self.label_ai_tag_sentence.pack(fill="x", padx=10, pady=2)
        self.label_body_summary.pack(fill="x", padx=10, pady=2)

    def _refresh_emails(self):
        self.refreshed_all_emails = get_all_emails()

        if self.refreshed_all_emails == self.all_emails:
            return

        self.all_emails = self.refreshed_all_emails

        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for email in self.all_emails:
            self.treeview.insert("", "end", iid=email["id"], values=(email["sender"], email["subject"], email["date_received"]))

        self.root.after(60000, self._refresh_emails))