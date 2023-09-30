import json


class DashboardButton:
    def __init__(self, root, title, domain, username, domain_controller):
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

    @staticmethod
    def listToJson(button_list):
        # Create a list to store the JSON representations of buttons
        json_button_list = []
        for button in button_list:
            # Create a dictionary with the relevant attributes
            button_dict = {
                "title": button.title,
                "domain": button.domain,
                "username": button.username,
                "domain_controller": button.domain_controller
            }
            json_button_list.append(button_dict)
        # Convert the list of dictionaries to a JSON string
        jsonStr = json.dumps(json_button_list)
        return jsonStr

    @staticmethod
    def listFromJson(jsonStr):
        # Parse the JSON string into a list of dictionaries
        json_button_list = json.loads(jsonStr)
        # Create a list of DashboardButton instances from the dictionaries
        button_list = []
        for button_dict in json_button_list:
            button = DashboardButton(
                root='',  # You can set root to an appropriate value
                title=button_dict["title"],
                domain=button_dict["domain"],
                username=button_dict["username"],
                domain_controller=button_dict["domain_controller"]
            )
            button_list.append(button)
        return button_list

    def toJson(self):
        # Create a dictionary with the relevant attributes
        button_dict = {
            "title": self.title,
            "domain": self.domain,
            "username": self.username,
            "domain_controller": self.domain_controller
        }
        # Convert the dictionary to a JSON string
        jsonStr = json.dumps(button_dict)
        return jsonStr

    @classmethod
    def fromJson(cls, jsonStr):
        # Parse the JSON string into a dictionary
        button_dict = json.loads(jsonStr)
        # Create a new DashboardButton instance using the dictionary values
        return cls(
            root='',  # You can set root to an appropriate value
            title=button_dict["title"],
            domain=button_dict["domain"],
            username=button_dict["username"],
            domain_controller=button_dict["domain_controller"]
        )


# Usage example
button1 = DashboardButton(root='', domain='', title='My Button 1',
                          username='User 1', domain_controller='Controller 1')

button2 = DashboardButton(root='', domain='', title='My Button 2',
                          username='User 2', domain_controller='Controller 2')

button_list = [button1, button2]

# Convert the list of buttons to JSON
jsonStr = DashboardButton.listToJson(button_list)

# Create a new list of buttons from JSON
new_button_list = DashboardButton.listFromJson(jsonStr)

# Access button titles in the new list
for button in new_button_list:
    print(button.title)

# Create a list of 10 buttons
button_list = []
for i in range(1, 11):
    button = DashboardButton(
        root='',  # You can set root to an appropriate value
        title=f'My Button {i}',
        domain=f'Domain {i}',
        username=f'User {i}',
        domain_controller=f'Controller {i}'
    )
    button_list.append(button)

# Convert the list of buttons to JSON
jsonStr = DashboardButton.listToJson(button_list)

# Specify the filename where you want to save the JSON data
filename = 'file.json'

# Open the file in write mode and save the JSON data
with open(filename, 'w') as file:
    # Use indent=4 for pretty formatting (optional)
    json.dump(json.loads(jsonStr), file, indent=4)

print(f'Saved {len(button_list)} buttons to {filename}')
# This code will create a list of 10 buttons, convert them to JSON, and save them to a file named file.json.
