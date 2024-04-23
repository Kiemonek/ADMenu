"""This module gets the buttons from the database."""
import json
import os
import utilities.constants as constants
from utilities.resource_path import ResourcePath


class GetButtons:
    """A class to represent the utilities of the application."""

    def __init__(self, id_button, root, title, domain, username,
                 domain_controller):
        self.id_button = id_button
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

    def get_button_list(self):
        """This method gets the button list from the database."""
        filename = ResourcePath.get_resource_path(self, constants.DBFILENAME)
        button_list = []

        if not os.path.exists(filename):
            database = open(filename, "a", encoding="utf-8")
            database.close()

        elif os.path.getsize(filename) > 0:

            database = open(filename, "r", encoding="utf-8")
            data = json.load(database)
            for item in data:
                button = GetButtons(
                    id_button=item['id_button'],
                    root=None,
                    title=item['title'],
                    domain=item['domain'],
                    username=item['username'],
                    domain_controller=item['domain_controller'])
                button_list.append(button)
            database.close()

        return button_list
