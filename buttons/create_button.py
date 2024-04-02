"""This module contains the ButtonBuilder class, which is responsible for creating buttons."""
import tkinter as tk
from app import constants
from utilities.calculate_position import CalculatePosition


class ButtonCreator:
    """A class to represent the button creator."""

    def __init__(self, frame, text, command):
        self.frame = frame
        self.text = text
        self.command = command

    def create_button(self,
                      frame,
                      text,
                      command,
                      id_button=None,
                      rel_x=None,
                      rel_y=None):
        """This method creates a button."""

        if id_button is not None and rel_x is None and rel_y is None:

            rel_width = 0.16
            rel_height = 0.095
            rel_x = CalculatePosition.calculate_rel_x(self, id_button)
            rel_y = CalculatePosition.calculate_rel_y(self, id_button)

        elif id_button is None and rel_x is not None and rel_y is None:
            rel_width = 0.24
            rel_height = 0.8
            rel_y = 0.09

        else:
            rel_width = 0.25
            rel_height = 0.08

        button = tk.Button(frame,
                           text=text,
                           bg=constants.BTN_BG_CLR,
                           fg=constants.BTN_FG_CLR,
                           font=constants.BTN_FONT_DETAILS,
                           activebackground=constants.BTN_ACTIVE_BG_CLR,
                           command=command)

        button.place(relwidth=rel_width,
                     relheight=rel_height,
                     anchor="n",
                     relx=rel_x,
                     rely=rel_y)
