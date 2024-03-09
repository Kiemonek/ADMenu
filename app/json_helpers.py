import json


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
        # Create a list to store the JSON representations of buttons
        json_button_list = []
        for button in button_list:
            # Create a dictionary with the relevant attributes
            button_dict = {
                "id_button": button.id_button,
                "title": button.title,
                "domain": button.domain,
                "username": button.username,
                "domain_controller": button.domain_controller
            }
            json_button_list.append(button_dict)
        # Convert the list of dictionaries to a JSON string
        jsonStr = json.dumps(json_button_list)
        return jsonStr

    def to_json(self):
        # Create a dictionary with the relevant attributes
        button_dict = {
            "id_button": self.id_button,
            "title": self.title,
            "domain": self.domain,
            "username": self.username,
            "domain_controller": self.domain_controller
        }
        # Convert the dictionary to a JSON string
        jsonStr = json.dumps(button_dict)
        return jsonStr

    @staticmethod
    def list_from_json(jsonStr):
        # Parse the JSON string into a list of dictionaries
        json_button_list = json.loads(jsonStr)
        # Create a list of Utilities instances from the dictionaries
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
    def from_json(cls, jsonStr):
        # Parse the JSON string into a dictionary
        button_dict = json.loads(jsonStr)
        # Create a new Utilities instance using the dictionary values
        return cls(id_button=button_dict["id_button"],
                   root=None,
                   title=button_dict["title"],
                   domain=button_dict["domain"],
                   username=button_dict["username"],
                   domain_controller=button_dict["domain_controller"])


# NOTE: Database Functions

    def save_changes_to_db(button_list):

        jsonStr = JsonHelpers.list_to_json(button_list)
        filename = 'BD.json'

        with open(filename, 'w') as file:
            json.dump(json.loads(jsonStr), file, indent=4)

    def removeButtonFromDB(frame, button_id):
        filename = "BD.json"
        with open(filename, 'r') as f:
            data = json.load(f)

        data = [button for button in data if button['id_button'] != button_id]

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        Utilities.show_button_list(frame, "rm")
