"""This module creates the button details top_frame. It is used to add or modify a button."""
import tkinter as tk
from tkinter import Entry, Label, Button
from app.save_button import SaveButton as svb
from app.get_buttons import GetButtons as gb
from app.clear_frame import ClearFrame as cf


class ButtonDetails:
    """This class creates the button details top_frame. It is used to add or modify a button."""

    def __init__(self, top_frame, button_id=None):
        self.top_frame = top_frame
        self.button_id = button_id

    #FIXME: This is not working
    def button_details(self, top_frame, button_id=None):
        """This method creates the buttun top_frame. It is used to add or modify a button."""
        cf.clear_frame(self, top_frame)

        if button_id is None:
            text = "Add New Button"
        else:
            text = "Modify Button"

        label = tk.Label(top_frame,
                         text=text,
                         fg='#838383',
                         bg='#1E1E1E',
                         font=("Microsoft YaHei", 12, "bold"))
        label.place(relwidth=1, relheight=0.1, relx=0.5, anchor="n")

        entry_dict = {
            "LabelName": Label(top_frame, text="Name:"),
            "title": Entry(top_frame),
            "LabelDomain": Label(top_frame, text="Domain:"),
            "domain": Entry(top_frame),
            "LabelUsername": Label(top_frame, text="Login:"),
            "username": Entry(top_frame),
            "LabelServer": Label(top_frame, text="Domain Controller:"),
            "domain_controller": Entry(top_frame),
        }
        if button_id is None:

            entry_dict["title"].insert(0, "Company A")
            entry_dict["domain"].insert(0, "companya.com")
            entry_dict["username"].insert(0, "user1")
            entry_dict["domain_controller"].insert(0, "192.168.21.37")

        else:
            current_data = gb.get_button_list(self)
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
            entry_dict[item].place(relwidth=0.5, relheight=0.1, relx=0.25)

        def get_entries(entry_dict):
            entry_data = {}
            for item in entry_dict:
                if not item[0:5] == "Label":
                    entry_data[item] = entry_dict[item].get()
            return entry_data

        save_button = Button(
            top_frame,
            text="SAVE",
            command=lambda: [
                svb.save_button(top_frame, get_entries(entry_dict), button_id
                                if button_id is not None else None),
            ])
        save_button.place()
