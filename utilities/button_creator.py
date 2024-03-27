"""This module contains the ButtonBuilder class, which is responsible for creating buttons."""
import tkinter as tk
from utilities import constants


class ButtonCreator:
    """A class to represent the button creator."""

    def __init__(self, frame, text, command):
        self.frame = frame
        self.text = text
        self.command = command

    def create_button(self, frame, text, command):
        """This method creates a button."""

        return tk.Button(frame,
                         text=text,
                         bg=constants.BTN_BG_CLR,
                         fg=constants.BTN_FG_CLR,
                         font=constants.FONT_DETAILS,
                         activebackground=constants.BTN_ACTIVE_BG_CLR,
                         command=command)
