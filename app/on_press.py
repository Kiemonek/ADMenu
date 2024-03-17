"""This module is used to create buttons with different commands depending on the option selected"""
import tkinter as tk
from app.button_details import ButtonDetails
from database.json_helpers import JsonHelpers


class OnPress:
    """This class is used to create buttons with different commands depending on the option."""

    def __init__(self, frame, option, items):
        self.frame = frame
        self.option = option
        self.items = items

    def on_pressed(self, items, frame, option):
        """This method creates buttons with different commands depending on the option selected."""
        if option == "rm":
            return tk.Button(
                frame,
                text=items.title,
                command=lambda: [
                    JsonHelpers.remove_button_from_db(self, items.id_button),
                    ShowButtons.show_button_list(self, frame, "rm")
                ],
            )
        elif option == "mod":
            return tk.Button(
                frame,
                text=items.title,
                command=lambda: [
                    ButtonDetails.button_details(self, frame, items.id_button)
                    #FIXME: This is not working
                ],
            )
        elif option == "cmd":
            return tk.Button(
                frame,
                text=items.title,
                command=lambda: [
                    print('runas /netonly /user:' + items.domain + "\\" + items
                          .username + ' "mmc dsa.msc /server=' + items.
                          domain_controller + '" ')
                ],
            )
