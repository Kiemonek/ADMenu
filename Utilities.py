import json
import os
from tkinter import *
from tkinter.ttk import *


class Utilities:
    # Button dashboard initializer
    def __init__(self, id, root, title, domain, username, domain_controller):
        self.id = id
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

# NOTE: Main Frame

    def mainFrame(frame):

        Utilities.showButtonList(frame, "cmd")

        # Usable Buttons
        add_button = Button(frame,
                            text="Add New Button",
                            command=lambda: [Utilities.addButton(frame)])
        add_button.pack()
        mod_button = Button(frame,
                            text="Modify Buttons",
                            command=lambda: [Utilities.modifyButtons(frame)])
        mod_button.pack()
        rem_button = Button(frame,
                            text="Remove Button",
                            command=lambda: [Utilities.removeButton(frame)])
        rem_button.pack()

# NOTE: Add Button Frame

    def addButton(frame):

        Utilities.buttonDetails(frame)

# NOTE: Remove Button Frame

    def removeButton(frame):

        Utilities.showButtonList(frame, "rm")

        Utilities.backButton(frame)

# NOTE: Modify Button Frame

    def modifyButtons(frame):

        Utilities.showButtonList(frame, "mod")

        Utilities.backButton(frame)

#NOTE: JSON Functions

    @staticmethod
    def listToJson(button_list):
        # Create a list to store the JSON representations of buttons
        json_button_list = []
        for button in button_list:
            # Create a dictionary with the relevant attributes
            button_dict = {
                "id": button.id,
                "title": button.title,
                "domain": button.domain,
                "username": button.username,
                "domain_controller": button.domain_controller
            }
            json_button_list.append(button_dict)
        # Convert the list of dictionaries to a JSON string
        jsonStr = json.dumps(json_button_list)
        return jsonStr

    def toJson(self):
        # Create a dictionary with the relevant attributes
        button_dict = {
            "id": self.id,
            "title": self.title,
            "domain": self.domain,
            "username": self.username,
            "domain_controller": self.domain_controller
        }
        # Convert the dictionary to a JSON string
        jsonStr = json.dumps(button_dict)
        return jsonStr

    @staticmethod
    def listFromJson(jsonStr):
        # Parse the JSON string into a list of dictionaries
        json_button_list = json.loads(jsonStr)
        # Create a list of Utilities instances from the dictionaries
        button_list = []
        for button_dict in json_button_list:
            button = Utilities(
                id=button_dict["id"],
                root=None,
                title=button_dict["title"],
                domain=button_dict["domain"],
                username=button_dict["username"],
                domain_controller=button_dict["domain_controller"])
            button_list.append(button)
        return button_list

    @classmethod
    def fromJson(cls, jsonStr):
        # Parse the JSON string into a dictionary
        button_dict = json.loads(jsonStr)
        # Create a new Utilities instance using the dictionary values
        return cls(id=button_dict["id"],
                   root=None,
                   title=button_dict["title"],
                   domain=button_dict["domain"],
                   username=button_dict["username"],
                   domain_controller=button_dict["domain_controller"])

# NOTE: Database Functions

    def saveChangesToDB(button_list):

        # Convert the list of buttons to JSON
        jsonStr = Utilities.listToJson(button_list)

        # Specify the filename where you want to save the JSON data
        filename = 'BD.json'

        # Open the file in write mode and save the JSON data
        with open(filename, 'w') as file:
            # Use indent=4 for pretty formatting
            json.dump(json.loads(jsonStr), file, indent=4)

    def removeButtonFromDB(frame, button_id):
        filename = "BD.json"
        with open(filename, 'r') as f:
            data = json.load(f)

        data = [button for button in data if button['id'] != button_id]
        # Write the data back to the file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        Utilities.removeButton(frame)

# NOTE: Utility Functions

# Return list of available buttons

    def getButtonList():
        filename = "BD.json"
        database = open(filename, "r")
        data = json.loads(database.read())

        button_list = []
        for item in data:
            button = Utilities(id=item['id'],
                               root=None,
                               title=item['title'],
                               domain=item['domain'],
                               username=item['username'],
                               domain_controller=item['domain_controller'])
            button_list.append(button)
        database.close()
        return button_list

    def showButtonList(frame, option):
        Utilities.clear_frame(frame)
        # Implement list from json
        button_list = Utilities.getButtonList()

        for items in button_list:

            def onPressed(x=items):
                if option == "rm":
                    return Utilities.removeButtonFromDB(frame, x.id)
                elif option == "mod":
                    return Utilities.buttonDetails(frame, x.id)
                elif option == "cmd":
                    print('runas /netonly /user:' + x.domain + "\\" +
                          x.username + ' "mmc dsa.msc /server=' +
                          x.domain_controller + '" ')
                else:
                    print("Error: Option not found")

            button = Button(frame, text=items.title, command=onPressed)
            button.pack()

    def buttonDetails(frame, button_id=None):

        Utilities.clear_frame(frame)

        entry_dict = {
            "LabelName": Label(frame, text="Name:"),
            "title": Entry(frame),
            "LabelDomain": Label(frame, text="Domain:"),
            "domain": Entry(frame),
            "LabelUsername": Label(frame, text="Login:"),
            "username": Entry(frame),
            "LabelServer": Label(frame, text="Domain Controller:"),
            "domain_controller": Entry(frame),
        }
        if button_id is None:

            entry_dict["title"].insert(0, "Company A")
            entry_dict["domain"].insert(0, "companya.com")
            entry_dict["username"].insert(0, "user1")
            entry_dict["domain_controller"].insert(0, "192.168.21.37")

        else:
            current_data = Utilities.getButtonList()
            for items in current_data:
                if items.id == button_id:
                    button_data = {
                        "title": items.title,
                        "domain": items.domain,
                        "username": items.username,
                        "domain_controller": items.domain_controller,
                    }

            entry_dict["title"].insert(0, button_data["title"])
            entry_dict["domain"].insert(0, button_data["domain"])
            entry_dict["username"].insert(0, button_data["username"])
            entry_dict["domain_controller"].insert(
                0, button_data["domain_controller"])

        for item in entry_dict:
            entry_dict[item].pack()

        def getEntries(entry_dict=entry_dict):
            entry_data = {}
            for item in entry_dict:
                if not item[0:5] == "Label":
                    entry_data[item] = entry_dict[item].get()
            return entry_data

        save_button = Button(frame,
                             text="SAVE",
                             command=lambda: [
                                 Utilities.saveButton(
                                     getEntries(), button_id
                                     if button_id is not None else None),
                                 Utilities.modifyButtons(frame)
                             ])
        save_button.pack()

        Utilities.backButton(frame)

    def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def backButton(frame):

        exit_button = Button(frame,
                             text="FUCK GO BACK",
                             command=lambda: [Utilities.mainFrame(frame)])
        exit_button.pack()

    def saveButton(entry_data, button_id=None):
        if button_id is None:
            append_button = Utilities.getButtonList()
        else:
            current_data = Utilities.getButtonList()
            append_button = [
                button for button in current_data if not button.id == button_id
            ]

        new_title = entry_data["title"]
        new_domain = entry_data["domain"]
        new_username = entry_data["username"]
        new_domain_controller = entry_data["domain_controller"]

        # Generate a unique id for the button
        if button_id is None:
            max_id = max(button.id for button in append_button)
            button_id = max_id + 1
        elif button_id is not None:
            button_id = button_id
        else:
            button_id = 0

        button = Utilities(id=button_id,
                           root='',
                           title=new_title,
                           domain=new_domain,
                           username=new_username,
                           domain_controller=new_domain_controller)
        append_button.append(button)
        append_button = sorted(append_button, key=lambda x: x.id)

        Utilities.saveChangesToDB(append_button)


# This code will create a list of 10 buttons, convert them to JSON, and save them to a file named file.json.
# Create a list of 10 buttons
# button_list = []  # Define the button_list variable
# for i in range(1, 11):
#     button = Utilities(
#         id=i,
#         root='',  # You can set root to an appropriate value
#         title=f'My Button {i}',
#         domain=f'Domain {i}',
#         username=f'User {i}',
#         domain_controller=f'Controller {i}'
#     )
#     print(button.title)
#     button_list.append(button)
#     Utilities.saveChangesToDB(button_list)
