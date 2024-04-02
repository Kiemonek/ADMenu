"""This module creates an entry."""
import tkinter as tk
from app import constants


class EntryCreator:
    """A class to represent the entry creator."""

    def __init__(self, frame):
        self.frame = frame

    def create_entry(self, frame, rel_y, validation=None):
        """This method creates an entry."""

        def validate_entry(P):
            """This method validates the entry."""
            if len(P) > 12:
                return False
            else:
                return True

        entry = tk.Entry(frame,
                         font=constants.LBL_FONT_DETAILS,
                         bg=constants.LBL_BG_CLR,
                         fg=constants.LBL_FG_CLR,
                         justify="center",
                         borderwidth=0)

        if validation is not None:
            vcmd = (frame.register(validate_entry), '%P')
            entry.config(validate="key", validatecommand=vcmd)

        entry.place(relwidth=0.35,
                    relheight=0.1,
                    relx=0.75,
                    rely=rel_y,
                    anchor="n")

        rel_y += 0.08
        label = tk.Label(frame, background="black")
        label.place(relwidth=0.35,
                    relheight=0.001,
                    relx=0.75,
                    rely=rel_y,
                    anchor="n")
        return entry
