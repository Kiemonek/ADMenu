"""This module contains the ResourcePath class."""
import os
import sys
from utilities import constants


class ResourcePath:
    """A class to represent the utilities of the application."""

    def __init__(self, relative_path):
        self.relative_path = relative_path

    def get_resource_path(self, relative_path):
        """This method gets the resource path of the application."""
        app_data_path = os.path.join(
            os.path.join(os.getenv('PROGRAMDATA'), constants.FILEPATH))
        if not os.path.exists(app_data_path):
            os.makedirs(app_data_path)
        return os.path.join(os.getenv('PROGRAMDATA'), relative_path)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            base_path = getattr(sys, '_MEIPASS',
                                os.path.dirname(os.path.abspath(__file__)))
        except FileNotFoundError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
