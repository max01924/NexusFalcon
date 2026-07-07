import tkinter as tk
from tkinter import ttk


class NotificationPopup:
    WINDOW_WIDTH = 350
    COMPACT_HEIGHT = 120
    EXPANDED_HEIGHT = 300

    def __init__(self, sender, subject, ai_tag_sentence, body_summary):
        """
        Args:
            sender: Absender der Mail
            subject: Betreff
            ai_tag_sentence: KI-Ein-Satz-Zusammenfassung
            body_summary: Liste von Stichpunkten
        """
        self.sender = sender
        self.subject = subject
        self.ai_tag_sentence = ai_tag_sentence
        self.body_summary = "\n".join(body_summary)

        self.is_expanded = False
        self.timer_id = None

        self.root = tk.Tk()
        self.root.title("")
        self._force_topmost()
        self.root.overrideredirect(True)

        self._position_top_right()
        self._compact_view()
        self._expanded_view()
        self._event_hover()
        self._start_timer()
        self.root.mainloop()

    def _position_top_right(self):
        screen_width = self.root.winfo_screenwidth()
        margin = 20
        x = screen_width - self.WINDOW_WIDTH - margin
        y = margin
        self.root.geometry(
            f"{self.WINDOW_WIDTH}x{self.COMPACT_HEIGHT}+{x}+{y}"
        )

    def _force_topmost(self):
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()
        self.root.after(500, self._force_topmost)

    def _compact_view(self):
        self.header_label = ttk.Label(
            self.root,
            text="New Mail",
            anchor="w",
        )
        self.sender_label = ttk.Label(
            self.root,
            text=self.sender,
            anchor="w",
        )
        self.subject_label = ttk.Label(
            self.root,
            text=self.subject,
            anchor="w",
        )
        self.ai_tag_sentence_label = ttk.Label(
            self.root,
            text=self.ai_tag_sentence,
            anchor="w",
        )

        self.header_label.pack(fill="x", padx=10, pady=2)
        self.sender_label.pack(fill="x", padx=10, pady=2)
        self.subject_label.pack(fill="x", padx=10, pady=2)
        self.ai_tag_sentence_label.pack(fill="x", padx=10, pady=2)

    def _expanded_view(self):
        self.body_summary_label = ttk.Label(
            self.root,
            text=self.body_summary,
            anchor="w",
            wraplength=self.WINDOW_WIDTH - 20,
        )

    def _event_hover(self):
        hover_widgets = [
            self.root,
            self.header_label,
            self.sender_label,
            self.subject_label,
            self.ai_tag_sentence_label,
            self.body_summary_label,
        ]
        for widget in hover_widgets:
            widget.bind("<Enter>", self._on_hover)
            widget.bind("<Leave>", self._on_leave)

    def _cancel_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def _start_timer(self, delay_ms=10000):
        self._cancel_timer()
        self.timer_id = self.root.after(delay_ms, self._hide_window)

    def _is_cursor_inside_popup(self):
        widget = self.root.winfo_containing(
            self.root.winfo_pointerx(),
            self.root.winfo_pointery(),
        )
        current = widget
        while current is not None:
            if current == self.root:
                return True
            current = current.master
        return False

    def _on_hover(self, _event):
        self._cancel_timer()
        if self.is_expanded:
            return

        self.is_expanded = True
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.EXPANDED_HEIGHT}")
        self.body_summary_label.pack(fill="x", padx=10, pady=2)

    def _on_leave(self, _event):
        self.root.after(50, self._check_leave)

    def _check_leave(self):
        if self._is_cursor_inside_popup():
            return

        if self.is_expanded:
            self.is_expanded = False
            self.body_summary_label.pack_forget()
            self.root.geometry(f"{self.WINDOW_WIDTH}x{self.COMPACT_HEIGHT}")

        self._start_timer(5000)

    def _hide_window(self):
        self.timer_id = None
        self.root.destroy()
