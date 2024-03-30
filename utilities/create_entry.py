"""This module creates an entry."""
import tkinter as tk
from utilities import constants


class EntryCreator:
    """A class to represent the entry creator."""

    def __init__(self, frame):
        self.frame = frame

    def create_entry(self, frame):
        """This method creates an entry."""
        entry = tk.Entry(frame,
                         font=constants.FONT_DETAILS,
                         bg=constants.LBL_BG_CLR,
                         fg=constants.LBL_FG_CLR,
                         justify="center",
                         borderwidth=0),
        return entry
