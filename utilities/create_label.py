"""This module contains the label creator class."""
import tkinter as tk
from app import constants


class LabelCreator:
    """A class to represent the label creator."""

    def __init__(self, frame, text):
        self.frame = frame
        self.text = text

    def create_label(self, frame, text, option=None, rel_x=None, rel_y=None):
        """This method creates a label."""
        font = constants.LBL_FONT_DETAILS
        bg_color = constants.LBL_TOP_BG_CLR
        fg_color = constants.LBL_TOP_FG_CLR

        if option == constants.OPTION_RM:
            fg_color = constants.LBL_REM_FG_CLR
        elif option == constants.OPTION_MOD:
            fg_color = constants.LBL_MOD_FG_CLR
        elif option == constants.OPTION_ADD:
            fg_color = constants.LBL_ADD_FG_CLR
        elif option == constants.OPTION_CMD:
            fg_color = constants.LBL_CONNECT_FG_CLR
        elif option == constants.OPTION_TOP:
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
