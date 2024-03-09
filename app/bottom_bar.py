"""This module creates the bottom bar of the application with buttons to interact."""
import tkinter as tk
from app.utilities import Utilities as util
from app.button_details import ButtonDetails as details


class BottomBar:
    """This class creates the bottom bar of the application with buttons to interact."""

    def __init__(self, top_frame, bottom_frame):
        self.top_frame = top_frame
        self.bottom_frame = bottom_frame

    def bottom_bar(self, top_frame, bottom_frame):
        """This method creates the bottom bar of the application with buttons to interact."""

        dsa_button = tk.Button(
            bottom_frame,
            text="CONNECT",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [util.show_button_list(top_frame, "cmd")])
        dsa_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.125,
                         rely=0.15)

        add_button = tk.Button(
            bottom_frame,
            text="ADD",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [details.button_details(top_frame, None)])
        add_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.375,
                         rely=0.15)

        mod_button = tk.Button(
            bottom_frame,
            text="MODIFY",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [util.show_button_list(top_frame, "mod")])

        mod_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.625,
                         rely=0.15)

        rem_button = tk.Button(
            bottom_frame,
            text="REMOVE",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [util.show_button_list(top_frame, "rm")])
        rem_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.875,
                         rely=0.15)
