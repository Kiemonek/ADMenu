"""This module contains the label creator class."""
import tkinter as tk
from utilities import constants


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
            bg=constants.LBL_BG_CLR,
            fg=constants.BTN_FG_CLR,
            font=constants.FONT_DETAILS,
        )
