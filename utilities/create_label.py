"""This module contains the label creator class."""
import tkinter as tk
from utilities import constants


class LabelCreator:
    """A class to represent the label creator."""

    def __init__(self, frame, text):
        self.frame = frame
        self.text = text

    def create_top_label(self, frame, text):
        """This method creates a label."""
        label = tk.Label(
            frame,
            text=text,
            bg=constants.TOP_LBL_BG_CLR,
            fg=constants.TOP_LBL_FG_CLR,
            font=constants.FONT_DETAILS,
        )

        label.place(relwidth=1, relheight=0.1, relx=0.5, anchor="n")

    def create_label(self, frame, text, rel_x=None, rel_y=None):
        """This method creates a label."""
        label = tk.Label(
            frame,
            text=text,
            bg=constants.LBL_BG_CLR,
            fg=constants.LBL_FG_CLR,
            font=constants.FONT_DETAILS,
        )
        if rel_x is None:
            label.place(relx=0.1, rely=rel_y)
        else:
            label.place(relx=rel_x, rely=rel_y, anchor="n")
        return label
