"""This module creates the bottom bar of the application with buttons to interact."""
import tkinter as tk
from app.utilities import Utilities as util


class BottomBar:
    """This class creates the bottom bar of the application with buttons to interact."""

    def __init__(self, frame, bottom_bar):

        dsa_button = tk.Button(
            bottom_bar,
            text="CONNECT",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [util.show_button_list(frame, "cmd")])
        dsa_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.125,
                         rely=0.15)

        add_button = tk.Button(bottom_bar,
                               text="ADD",
                               bg='#1E1E1E',
                               fg='#838383',
                               font=("Microsoft YaHei", 12, "bold"),
                               activebackground='#838383',
                               command=lambda: [util.buttonDetails(frame)])
        add_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.375,
                         rely=0.15)

        mod_button = tk.Button(
            bottom_bar,
            text="MODIFY",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [util.show_button_list(frame, "mod")])

        mod_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.625,
                         rely=0.15)

        rem_button = tk.Button(
            bottom_bar,
            text="REMOVE",
            bg='#1E1E1E',
            fg='#838383',
            font=("Microsoft YaHei", 12, "bold"),
            activebackground='#838383',
            command=lambda: [util.show_button_list(frame, "rm")])
        rem_button.place(relwidth=0.23,
                         relheight=0.7,
                         anchor='n',
                         relx=0.875,
                         rely=0.15)
