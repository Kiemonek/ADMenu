"""This module creates the bottom bar of the application with buttons to interact."""
from buttons.create_button import ButtonCreator
from app.top_bar import TopBar
import utilities.constants as constants


class BottomBar:
    """This class creates the bottom bar of the application with buttons to interact."""

    def __init__(self, top_frame, bottom_frame):
        self.top_frame = top_frame
        self.bottom_frame = bottom_frame

    def bottom_bar(self, top_frame, bottom_frame):
        """This method creates the bottom bar of the application with buttons to interact."""

        button_bar_data = [
            (constants.BTN_CONNECT, lambda: TopBar.show_button_list(
                self, top_frame, constants.OPTION_CMD), 0.125),
            (constants.BTN_ADD,
             lambda: TopBar.button_details(self, top_frame, None), 0.375),
            (constants.BTN_MODIFY, lambda: TopBar.show_button_list(
                self, top_frame, constants.OPTION_MOD), 0.625),
            (constants.BTN_REMOVE, lambda: TopBar.show_button_list(
                self, top_frame, constants.OPTION_RM), 0.875)
        ]

        for text, command, rel_x in button_bar_data:
            ButtonCreator.create_button(self,
                                        bottom_frame,
                                        text,
                                        command,
                                        rel_x=rel_x)
