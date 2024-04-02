"""This module is used to show the buttons in the main frame."""
from utilities.create_label import LabelCreator
from utilities.clear_frame import ClearFrame
from database.json_helpers import JsonHelpers
from buttons.save_button import SaveButton
from buttons.get_buttons import GetButtons
from buttons.create_button import ButtonCreator
from entry.fill_entry import EntryFiller
from entry.create_entry import EntryCreator
from app import constants


class TopBar:
    """This class is used to show the buttons in the main frame."""

    def __init__(self, buttons):
        self.buttons = buttons

    def show_button_list(self, frame, option):
        """This method creates the button list frame. It is used to remove, modify or connect."""

        ClearFrame.clear_frame(self, frame)

        if option == "rm":
            text = constants.LBL_TOP_RM_TXT
        elif option == "mod":
            text = constants.LBL_TOP_MOD_TXT
        elif option == "cmd":
            text = constants.LBL_TOP_CMD_TXT

        LabelCreator.create_label(self, frame, text, option)

        button_list = GetButtons.get_button_list(self)

        if len(button_list) == 0:
            LabelCreator.create_label(self,
                                      frame,
                                      constants.LBL_NO_BTN_TXT,
                                      rel_x=0.5,
                                      rel_y=0.4)
            ButtonCreator.create_button(
                self,
                frame,
                constants.BTN_ADD_NEW_TXT,
                lambda: [TopBar.button_details(self, frame)],
                rel_x=0.5,
                rel_y=0.6)

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
            option = "add"
            text = constants.LBL_ADD_BTN_TXT
        else:
            option = "mod"
            text = constants.LBL_MOD_BTN_TXT

        LabelCreator.create_label(self, top_frame, text, option)

        label_dict = {}
        entry_dict = {}
        button_details = [
            ("LabelName", "title", "Insert Button Name:", 0.2, True),
            ("LabelDomain", "domain", "Insert Domain Name:", 0.35, None),
            ("LabelUsername", "username", "Insert Username:", 0.5, None),
            ("LabelController", "domain_controller",
             "Insert Domain Controller:", 0.65, None),
        ]

        for label, entry, text, rel_y, valid in button_details:
            label_dict[label] = LabelCreator.create_label(self,
                                                          top_frame,
                                                          text,
                                                          rel_y=rel_y)

            entry_dict[entry] = EntryCreator.create_entry(self,
                                                          top_frame,
                                                          rel_y,
                                                          validation=valid)

        EntryFiller.fill_entry(self, entry_dict, button_id)

        def get_entries(entry_dict):
            entry_data = {}
            for key in entry_dict.keys():
                entry_data[key] = entry_dict[key].get()

            return entry_data

        button_id = button_id if button_id is not None else None
        ButtonCreator.create_button(
            self,
            top_frame,
            constants.BTN_SAVE_TXT,
            lambda: [
                SaveButton.save_button(self, get_entries(entry_dict), button_id
                                       ),
                TopBar.process_status(self, top_frame, button_id)
            ],
            rel_x=0.5,
            rel_y=0.85)

        tester = GetButtons.get_button_list(self)
        if len(tester) >= 48 and button_id is None:

            TopBar.process_status(self, top_frame, "limit")

    def process_status(self, top_frame, option):
        """This method creates the shows after save."""
        ClearFrame.clear_frame(self, top_frame)

        label = constants.LBL_TOP_SUCCESS_TXT

        if option == "rm":
            text = "Button removed successfully!"
        elif option is None:
            text = "Button added successfully!"
        elif option == "limit":
            text = "List reached a limit of 48 buttons, remove one to add a new one."
            label = "Limit reached!"
        else:
            text = "Button modified successfully!"

        LabelCreator.create_label(self, top_frame, label, "top")
        ButtonCreator.create_button(
            self,
            top_frame,
            "OK",
            lambda: [TopBar.show_button_list(self, top_frame, "cmd")],
            rel_x=0.5,
            rel_y=0.6)
        LabelCreator.create_label(self, top_frame, text, rel_x=0.5, rel_y=0.4)
