"""This module contains the JSONHelpers class."""
import json
import utilities.constants as constants
from utilities.resource_path import ResourcePath


class JsonHelpers:
    """A class to represent the utilities of the application."""

    def __init__(self, id_button, root, title, domain, username,
                 domain_controller):
        self.id_button = id_button
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

    @staticmethod
    def list_to_json(button_list):
        """Create a list to store the JSON representations of buttons"""
        json_button_list = []
        for button in button_list:

            button_dict = {
                "id_button": button.id_button,
                "title": button.title,
                "domain": button.domain,
                "username": button.username,
                "domain_controller": button.domain_controller
            }
            json_button_list.append(button_dict)

        json_string = json.dumps(json_button_list)
        return json_string

    def save_changes_to_db(self, button_list):
        """Save the changes to the database"""
        json_string = JsonHelpers.list_to_json(button_list)
        filename = ResourcePath.get_resource_path(self, constants.DBFILENAME)

        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(json.loads(json_string), file, indent=4)

    def remove_button_from_db(self, button_id):
        """Remove a button from the database"""
        filename = ResourcePath.get_resource_path(self, constants.DBFILENAME)
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        data = [button for button in data if button['id_button'] != button_id]
        for i, button in enumerate(data):
            button['id_button'] = i

        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
