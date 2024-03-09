"""This module creates the button details frame. It is used to add or modify a button."""
import tkinter as tk
from tkinter import Entry, Label
from app.utilities import Utilities


class ButtonDetails:
    """This class creates the button details frame. It is used to add or modify a button."""

    def __init__(self, top_frame, button_id=None):
        self.frame = top_frame
        self.button_id = button_id

    def button_details(self, frame, button_id=None):
        """This method creates the button details frame. It is used to add or modify a button."""
        Utilities.clear_frame(frame)

        if button_id is None:
            text = "Add New Button"
        else:
            text = "Modify Button"

        label = tk.Label(frame,
                         text=text,
                         fg='#838383',
                         bg='#1E1E1E',
                         font=("Microsoft YaHei", 12, "bold"))
        label.place(relwidth=1, relheight=0.1, relx=0.5, anchor="n")

        entry_dict = {
            "LabelName": Label(frame, text="Name:"),
            "title": Entry(frame),
            "LabelDomain": Label(frame, text="Domain:"),
            "domain": Entry(frame),
            "LabelUsername": Label(frame, text="Login:"),
            "username": Entry(frame),
            "LabelServer": Label(frame, text="Domain Controller:"),
            "domain_controller": Entry(frame),
        }
        if button_id is None:

            entry_dict["title"].insert(0, "Company A")
            entry_dict["domain"].insert(0, "companya.com")
            entry_dict["username"].insert(0, "user1")
            entry_dict["domain_controller"].insert(0, "192.168.21.37")

        else:
            current_data = Utilities.getButtonList()
            for items in current_data:
                if items.id_button == button_id:
                    button_data = {
                        "title": items.title,
                        "domain": items.domain,
                        "username": items.username,
                        "domain_controller": items.domain_controller,
                    }

            entry_dict["title"].insert(0, button_data["title"])
            entry_dict["domain"].insert(0, button_data["domain"])
            entry_dict["username"].insert(0, button_data["username"])
            entry_dict["domain_controller"].insert(
                0, button_data["domain_controller"])

        for item in entry_dict:
            entry_dict[item].place()
