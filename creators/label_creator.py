"""This module contains the label creator class."""
import tkinter as tk
import creators.constants as cnst


class LabelCreator:
    """A class to represent the label creator."""

    def __init__(self, frame, text):
        self.frame = frame
        self.text = text

    def create_label(self, frame, text):
        """This method creates a label."""
        return tk.Label(
            frame,
            text=text,
            bg=cnst.LBL_BG_CLR,
            fg=cnst.BTN_FG_CLR,
            font=cnst.FONT_DETAILS,
        )
