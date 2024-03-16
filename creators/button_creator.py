"""This module contains the ButtonBuilder class, which is responsible for creating buttons."""
import tkinter as tk
import creators.constants as cnst


class ButtonCreator:
    """A class to represent the button creator."""

    def __init__(self, frame, text, command):
        self.frame = frame
        self.text = text
        self.command = command

    def create_button(self, frame, text, command):
        """This method creates a button."""
        # button = tk.Button(frame,
        #                    text=text,
        #                    bg=cnst.BTN_BG_CLR,
        #                    fg=cnst.BTN_FG_CLR,
        #                    font=cnst.FONT_DETAILS,
        #                    activebackground=cnst.BTN_ACTIVE_BG_CLR,
        #                    command=command)
        return tk.Button(frame,
                         text=text,
                         bg=cnst.BTN_BG_CLR,
                         fg=cnst.BTN_FG_CLR,
                         font=cnst.FONT_DETAILS,
                         activebackground=cnst.BTN_ACTIVE_BG_CLR,
                         command=command)
