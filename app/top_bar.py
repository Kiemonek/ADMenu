"""This module is used to show the buttons in the main frame."""
from utilities.create_label import LabelCreator
from utilities.clear_frame import ClearFrame
from database.json_helpers import JsonHelpers
from buttons.save_button import SaveButton
from buttons.get_buttons import GetButtons
from buttons.create_button import ButtonCreator
from entry.fill_entry import EntryFiller
from entry.create_entry import EntryCreator


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

        if len(button_list) == 0:
            LabelCreator.create_label(self, frame, "No buttons added yet", 0.5,
                                      0.4)
            ButtonCreator.create_utility_button(
                self, frame, "Add New Button",
                lambda: [TopBar.button_details(self, frame)], 0.5, 0.6)

        for items in button_list:

            def on_pressed(x=items):
                if option == "rm":
                    return JsonHelpers.remove_button_from_db(
                        self,
                        x.id_button), TopBar.process_status(self, frame, "rm")

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

        LabelCreator.create_top_label(self, top_frame, text)

        label_dict = {}
        entry_dict = {}
        button_details = [
            ("LabelName", "title", "Insert Button Name:", 0.2),
            ("LabelDomain", "domain", "Insert Domain Name:", 0.35),
            ("LabelUsername", "username", "Insert Username:", 0.5),
            ("LabelController", "domain_controller",
             "Insert Domain Controller:", 0.65),
        ]

        for label, entry, text, rel_y in button_details:
            label_dict[label] = LabelCreator.create_label(
                self, top_frame, text, None, rel_y)

            entry_dict[entry] = EntryCreator.create_entry(
                self, top_frame, rel_y)

        EntryFiller.fill_entry(self, entry_dict, button_id)

        def get_entries(entry_dict):
            entry_data = {}
            for key in entry_dict.keys():
                entry_data[key] = entry_dict[key].get()

            return entry_data

        button_id = button_id if button_id is not None else None
        ButtonCreator.create_utility_button(
            self, top_frame, "SAVE", lambda: [
                SaveButton.save_button(self, get_entries(entry_dict), button_id
                                       ),
                TopBar.process_status(self, top_frame, button_id)
            ], 0.5, 0.85)

    def process_status(self, top_frame, option):
        """This method creates the shows after save."""
        ClearFrame.clear_frame(self, top_frame)

        LabelCreator.create_top_label(self, top_frame, "Success!")

        if option == "rm":
            text = "Button removed successfully!"
            ButtonCreator.create_utility_button(
                self, top_frame, "OK",
                lambda: [TopBar.show_button_list(self, top_frame, "rm")], 0.5,
                0.6)
        elif option is None:
            text = "Button added successfully!"
            ButtonCreator.create_utility_button(
                self, top_frame, "OK",
                lambda: [TopBar.show_button_list(self, top_frame, "mod")], 0.5,
                0.6)
        else:
            text = "Button modified successfully!"
            ButtonCreator.create_utility_button(
                self, top_frame, "OK",
                lambda: [TopBar.button_details(self, top_frame)], 0.5, 0.6)

        LabelCreator.create_label(self, top_frame, text, 0.5, 0.4)
