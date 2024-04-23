"""This module contains the ResourcePath class."""
import os
from utilities import constants


class ResourcePath:
    """A class to represent the utilities of the application."""

    def __init__(self, relative_path):
        self.relative_path = relative_path

    def get_resource_path(self, relative_path):
        """This method gets the resource path of the application."""
        app_data_path = os.path.join(
            os.path.join(os.getenv('APPDATA'), constants.FILEPATH))
        if not os.path.exists(app_data_path):
            os.makedirs(app_data_path)
        return os.path.join(os.getenv('APPDATA'), relative_path)
