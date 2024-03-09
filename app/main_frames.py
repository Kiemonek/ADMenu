"""This module contains the Frame class which is used to create the main frame of the application."""
from app.utilities import Utilities
#FIXME: Remove the this file later


class MainFrame:
    """This class creates the main frame of the application."""

    def __init__(self, frame, helper):
        self.frame = frame
        self.helper = helper

    # NOTE: Main Frame

    def main_frame(self, frame, helper):
        """This method creates the main frame of the application."""

        Utilities.show_button_list(frame, helper)
