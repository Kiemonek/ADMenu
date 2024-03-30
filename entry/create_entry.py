"""This module creates an entry."""
import tkinter as tk
from entry import constants


class EntryCreator:
    """A class to represent the entry creator."""

    def __init__(self, frame):
        self.frame = frame

    def create_entry(self, frame, rel_y):
        """This method creates an entry."""
        entry = tk.Entry(frame,
                         font=constants.FONT_DETAILS,
                         bg=constants.LBL_BG_CLR,
                         fg=constants.LBL_FG_CLR,
                         justify="center",
                         borderwidth=0)

        entry.place(relwidth=0.4, relx=0.55, rely=rel_y)
        return entry
