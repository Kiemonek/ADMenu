"""This module contains the label creator class."""
import tkinter as tk
from utilities import constants


class LabelCreator:
    """A class to represent the label creator."""

    def __init__(self, frame, text):
        self.frame = frame
        self.text = text

    def create_label(self, frame, text, option=None, rel_x=None, rel_y=None):
        """This method creates a label."""
        font = constants.FONT_DETAILS
        bg_color = constants.TOP_LBL_BG_CLR
        fg_color = constants.TOP_LBL_FG_CLR

        if option == "rm":
            fg_color = constants.REM_LBL_FG_CLR
        elif option == "mod":
            fg_color = constants.MOD_LBL_FG_CLR
        elif option == "add":
            fg_color = constants.ADD_LBL_FG_CLR
        elif option == "cmd":
            fg_color = constants.CONNECT_LBL_FG_CLR
        elif option == "top":
            pass
        else:
            bg_color = constants.LBL_BG_CLR
            fg_color = constants.LBL_FG_CLR

        label = tk.Label(
            frame,
            text=text,
            bg=bg_color,
            fg=fg_color,
            font=font,
        )
        if rel_x is None and rel_y is None:
            label.place(relwidth=1, relheight=0.1, relx=0.5, anchor="n")
        elif rel_x is None:
            label.place(relx=0.1, rely=rel_y)
        else:
            label.place(relx=rel_x, rely=rel_y, anchor="n")

        return label
