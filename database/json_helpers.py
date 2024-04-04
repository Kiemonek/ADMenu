"""This module contains the JSONHelpers class."""
import json
from app import constants


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

#NOTE: JSON Functions

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

    def to_json(self):
        """Create a dictionary with the relevant attributes"""

        button_dict = {
            "id_button": self.id_button,
            "title": self.title,
            "domain": self.domain,
            "username": self.username,
            "domain_controller": self.domain_controller
        }

        json_string = json.dumps(button_dict)
        return json_string

    @staticmethod
    def list_from_json(json_string):
        """Parse the JSON string into a list of dictionaries"""
        json_button_list = json.loads(json_string)

        button_list = []
        for button_dict in json_button_list:
            button = JsonHelpers(
                id_button=button_dict["id_button"],
                root=None,
                title=button_dict["title"],
                domain=button_dict["domain"],
                username=button_dict["username"],
                domain_controller=button_dict["domain_controller"])
            button_list.append(button)
        return button_list

    @classmethod
    def from_json(cls, json_string):
        """Parse the JSON string into a dictionary"""
        button_dict = json.loads(json_string)
        return cls(id_button=button_dict["id_button"],
                   root=None,
                   title=button_dict["title"],
                   domain=button_dict["domain"],
                   username=button_dict["username"],
                   domain_controller=button_dict["domain_controller"])


# NOTE: Database Functions

    def save_changes_to_db(self, button_list):
        """Save the changes to the database"""
        json_string = JsonHelpers.list_to_json(button_list)
        filename = constants.FILENAME

        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(json.loads(json_string), file, indent=4)

    def remove_button_from_db(self, button_id):
        """Remove a button from the database"""
        filename = constants.FILENAME
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        data = [button for button in data if button['id_button'] != button_id]
        for i, button in enumerate(data):
            button['id_button'] = i

        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
