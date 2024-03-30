"""This module is used to show the buttons in the main frame."""
import tkinter as tk
import app.constants as constants
from utilities.create_label import LabelCreator
from utilities.clear_frame import ClearFrame
from database.json_helpers import JsonHelpers
from buttons.save_button import SaveButton
from buttons.get_buttons import GetButtons
from buttons.create_button import ButtonCreator
from utilities.create_entry import EntryCreator


class TopBar:
    """This class is used to show the buttons in the main frame."""

    def __init__(self, buttons):
        self.buttons = buttons

    def show_button_list(self, frame, option):
        """This method creates the button list frame. It is used to remove, modify or connect."""

        ClearFrame.clear_frame(self, frame)

        if option == "rm":
            text = "Choose and press button to remove"
        elif option == "mod":
            text = "Choose and press button to modify"
        elif option == "cmd":
            text = "Choose and press button to connect dsa"

        LabelCreator.create_top_label(self, frame, text)

        button_list = GetButtons.get_button_list(self)
        for items in button_list:

            def on_pressed(x=items):
                if option == "rm":
                    return JsonHelpers.remove_button_from_db(
                        self, x.id_button), TopBar.show_button_list(
                            self, frame, "rm")

                elif option == "mod":
                    return TopBar.button_details(self, frame, x.id_button)

                elif option == "cmd":
                    return print('runas /netonly /user:' + x.domain + "\\" +
                                 x.username + ' "mmc dsa.msc /server=' +
                                 x.domain_controller + '" ')

            ButtonCreator.create_button(self,
                                        frame,
                                        items.title,
                                        command=on_pressed,
                                        id_button=items.id_button)

    def button_details(self, top_frame, button_id=None):
        """This method creates the buttun top_frame. It is used to add or modify a button."""

        ClearFrame.clear_frame(self, top_frame)

        if button_id is None:
            text = "Add New Button"
        else:
            text = "Modify Button"
        #TODO: add next button

        LabelCreator.create_top_label(self, top_frame, text)

        label_dict = {}
        entry_dict = {}

        button_details = [("LabelName", "title", "Insert Button Name:"),
                          ("LabelDomain", "domain", "Insert Domain Name:"),
                          ("LabelUsername", "username", "Insert Username:"),
                          ("LabelController", "domain_controller",
                           "Insert Domain Controller:")]

        for label, entry, text in button_details:
            label_dict[label] = LabelCreator.create_label(
                self, top_frame, text)
            entry_dict[entry] = EntryCreator.create_entry(self, top_frame)

            # if button_id is None:
            #     entry.insert(0, "Company A")
            #     entry.insert(0, "companya.com")
            #     entry.insert(0, "user1")
            #     entry.insert(0, "

        if button_id is None:
            entry_dict["title"].insert(0, "Company A")
            entry_dict["domain"].insert(0, "companya.com")
            entry_dict["username"].insert(0, "user1")
            entry_dict["domain_controller"].insert(0, "192.168.21.37")
        else:
            current_data = GetButtons.get_button_list(self)
            current_data = GetButtons.get_button_list(self)
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

        entry_dict["LabelName"].place(relx=0.1, rely=0.2)
        entry_dict["title"].place(relx=0.5, rely=0.2)
        entry_dict["LabelDomain"].place(relx=0.1, rely=0.35)
        entry_dict["domain"].place(relx=0.5, rely=0.35)
        entry_dict["LabelUsername"].place(relx=0.1, rely=0.5)
        entry_dict["username"].place(relx=0.5, rely=0.5)
        entry_dict["LabelServer"].place(relx=0.1, rely=0.65)
        entry_dict["domain_controller"].place(relx=0.5, rely=0.65)

        def get_entries(entry_dict):
            entry_data = {}
            for item in entry_dict:
                if not item[0:5] == "Label":
                    entry_data[item] = entry_dict[item].get()

            return entry_data

        button_id = button_id if button_id is not None else None
        # save_button = ButtonCreator.create_button(
        #     self, top_frame, "SAVE", lambda: [
        #         SaveButton.save_button(top_frame, get_entries(entry_dict),
        #                                button_id),
        #         TopBar.button_details(self, top_frame)
        #     ])
        # save_button.place(relx=0.5,
        #                   rely=0.85,
        #                   relwidth=0.25,
        #                   relheight=0.08,
        #                   anchor="n")
