"""This module contains the ButtonBuilder class, which is responsible for creating buttons."""
import tkinter as tk
import utilities.constants as cnst


class ButtonCreator:
    """A class to represent the button builder."""

    def __init__(self, frame, text, command):
        self.frame = frame
        self.text = text
        self.command = command

    def create_button(self, frame, text, command):
        """This method creates a button."""
        return tk.Button(frame=frame,
                         text=text,
                         bg=cnst.BTN_BG_CLR,
                         fg=cnst.BTN_FG_CLR,
                         font=cnst.FONT_DETAILS,
                         activebackground=cnst.ACTIVE_BG_CLR,
                         command=command)
