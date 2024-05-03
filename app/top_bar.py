"""This module is used to show the buttons in the main frame."""
from command_executer.rsat_status import RsatStatus
from command_executer.dsa_connect import DSAConnect
from label.create_label import LabelCreator
from utilities.clear_frame import ClearFrame
from utilities.json_helpers import JsonHelpers
from buttons.save_button import SaveButton
from buttons.get_buttons import GetButtons
from buttons.create_button import ButtonCreator
from entry.fill_entry import EntryFiller
from entry.create_entry import EntryCreator
import utilities.constants as constants


class TopBar:
    """This class is used to show the buttons in the main frame."""

    def __init__(self, buttons):
        self.buttons = buttons

    def show_button_list(self, frame, option):
        """This method creates the button list frame. It is used to remove, modify or connect."""

        ClearFrame.clear_frame(self, frame)

        if option == constants.OPTION_RM:
            text = constants.TOP_RM
        elif option == constants.OPTION_MOD:
            text = constants.TOP_MOD
        elif option == constants.OPTION_CMD:
            text = constants.TOP_CMD

        LabelCreator.create_label(self, frame, text, option)
        RsatStatus.display_status(self, frame)

        button_list = GetButtons.get_button_list(self)

        if len(button_list) == 0:
            LabelCreator.create_label(self,
                                      frame,
                                      constants.STATUS_NO_BTN,
                                      rel_x=0.5,
                                      rel_y=0.4)
            ButtonCreator.create_button(
                self,
                frame,
                constants.BTN_ADD_NEW,
                lambda: [TopBar.button_details(self, frame)],
                rel_x=0.5,
                rel_y=0.6)

        for items in button_list:

            def on_pressed(x=items):
                if option == constants.OPTION_RM:
                    return JsonHelpers.remove_button_from_db(
                        self, x.id_button), TopBar.process_status(
                            self, frame, constants.OPTION_RM)

                elif option == constants.OPTION_MOD:
                    return TopBar.button_details(self, frame, x.id_button)

                elif option == constants.OPTION_CMD:
                    return DSAConnect.connect_dsa(self, x)

            ButtonCreator.create_button(self,
                                        frame,
                                        items.title,
                                        command=on_pressed,
                                        id_button=items.id_button)

    def button_details(self, top_frame, button_id=None):
        """This method creates the buttun top_frame. It is used to add or modify a button."""

        ClearFrame.clear_frame(self, top_frame)

        if button_id is None:
            option = constants.OPTION_ADD
            text = constants.TOP_ADD_BTN
        else:
            option = constants.OPTION_MOD
            text = constants.TOP_MOD_BTN

        LabelCreator.create_label(self, top_frame, text, option)
        RsatStatus.display_status(self, top_frame)

        label_dict = {}
        entry_dict = {}
        button_details = [
            ("LabelName", "title", constants.INSERT_TITLE, 0.2, True),
            ("LabelDomain", "domain", constants.INSERT_DOMAIN, 0.35, None),
            ("LabelUsername", "username", constants.INSERT_USERNAME, 0.5,
             None),
            ("LabelController", "domain_controller",
             constants.INSERT_CONTROLLER, 0.65, None),
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
            constants.BTN_SAVE,
            lambda: [
                SaveButton.save_button(self, get_entries(entry_dict), button_id
                                       ),
                TopBar.process_status(self, top_frame, button_id)
            ],
            rel_x=0.5,
            rel_y=0.85)

        tester = GetButtons.get_button_list(self)
        if len(tester) >= 48 and button_id is None:

            TopBar.process_status(self, top_frame, constants.OPTION_LIMIT)

    def process_status(self, top_frame, option):
        """This method creates the shows after save."""
        ClearFrame.clear_frame(self, top_frame)

        label = constants.TOP_SUCCESS

        if option == constants.OPTION_RM:
            text = constants.STATUS_RM
        elif option is None:
            text = constants.STATUS_ADD
        elif option == constants.OPTION_LIMIT:
            text = constants.STATUS_LIMIT
            label = constants.TOP_LIMIT
        else:
            text = constants.STATUS_MOD

        LabelCreator.create_label(self, top_frame, label, constants.OPTION_TOP)
        RsatStatus.display_status(self, top_frame)
        ButtonCreator.create_button(
            self,
            top_frame,
            constants.BTN_OK,
            lambda:
            [TopBar.show_button_list(self, top_frame, constants.OPTION_CMD)],
            rel_x=0.5,
            rel_y=0.6)
        LabelCreator.create_label(self, top_frame, text, rel_x=0.5, rel_y=0.4)
