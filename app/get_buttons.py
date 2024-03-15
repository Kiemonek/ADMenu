"""This module gets the buttons from the database."""
import json


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


# NOTE: Utility Functions

    def get_button_list(self):
        """This method gets the button list from the database."""
        filename = "BD.json"
        with open(filename, "r", encoding="utf-8") as database:
            data = json.load(database)

        button_list = []
        for item in data:
            button = GetButtons(id_button=item['id_button'],
                                root=None,
                                title=item['title'],
                                domain=item['domain'],
                                username=item['username'],
                                domain_controller=item['domain_controller'])
            button_list.append(button)
        return button_list
