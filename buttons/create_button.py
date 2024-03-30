"""This module contains the ButtonBuilder class, which is responsible for creating buttons."""
import tkinter as tk
from buttons import constants
from utilities.calculate_position import CalculatePosition


class ButtonCreator:
    """A class to represent the button creator."""

    def __init__(self, frame, text, command):
        self.frame = frame
        self.text = text
        self.command = command

    def create_button(self, frame, text, command, id_button):
        """This method creates a button."""

        button = tk.Button(frame,
                           text=text,
                           bg=constants.BTN_BG_CLR,
                           fg=constants.BTN_FG_CLR,
                           font=constants.FONT_DETAILS,
                           activebackground=constants.BTN_ACTIVE_BG_CLR,
                           command=command)

        rel_x = CalculatePosition.calculate_rel_x(self, id_button)
        rel_y = CalculatePosition.calculate_rel_y(self, id_button)

        button.place(relwidth=0.16,
                     height=40,
                     anchor="nw",
                     relx=rel_x,
                     rely=rel_y)

    def create_bottom_button(self, frame, text, command, rel_x):
        """This method creates a bottom bar button."""
        button = tk.Button(frame,
                           text=text,
                           bg=constants.BTN_BG_CLR,
                           fg=constants.BTN_FG_CLR,
                           font=constants.FONT_DETAILS,
                           activebackground=constants.BTN_ACTIVE_BG_CLR,
                           command=command)

        button.place(relwidth=0.23,
                     relheight=0.7,
                     anchor='n',
                     relx=rel_x,
                     rely=0.15)

    def create_utility_button(self, frame, text, command, rel_x, rel_y):
        """This method creates a utility button."""
        button = tk.Button(frame,
                           text=text,
                           bg=constants.BTN_BG_CLR,
                           fg=constants.BTN_FG_CLR,
                           font=constants.FONT_DETAILS,
                           activebackground=constants.BTN_ACTIVE_BG_CLR,
                           command=command)

        button.place(relwidth=0.25,
                     relheight=0.08,
                     anchor="n",
                     relx=rel_x,
                     rely=rel_y)
