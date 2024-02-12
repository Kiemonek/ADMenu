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

        Utilities.clear_frame(frame)

        entry_list = [
            "LabelName",
            "title",
            "LabelDomain",
            "domain",
            "LabelUsername",
            "username",
            "LabelServer",
            "domain_controller",
        ]

        entry_dict = {}

        for item in entry_list:

            def showItems(item):
                if item[0:5] == "Label":
                    entry_dict[item] = Label(frame, text=item + ":")
                else:
                    entry_dict[item] = Entry(frame)
                    entry_dict[item].insert(0, "test " + item)

                return entry_dict[item].pack()

            showItems(item)

        def getEntries(entry_list=entry_list, entry_dict=entry_dict):
            entry_data = {}
            for item in entry_list:
                if not item[0:5] == "Label":
                    entry_data[item] = entry_dict[item].get()
            return entry_data

        save_button = Button(
            frame,
            text="SAVE",
            command=lambda:
            [Utilities.saveButton(getEntries()),
             Utilities.mainFrame(frame)])
        save_button.pack()

        Utilities.backButton(frame)

    def saveButton(entry_data):

        append_button = Utilities.getButtonList()

        new_title = entry_data["title"]
        new_domain = entry_data["domain"]
        new_username = entry_data["username"]
        new_domain_controller = entry_data["domain_controller"]

        # Generate a unique id for the button
        if append_button:
            max_id = max(button.id for button in append_button)
            button_id = max_id + 1
        else:
            button_id = 0

        button = Utilities(id=button_id,
                           root='',
                           title=new_title,
                           domain=new_domain,
                           username=new_username,
                           domain_controller=new_domain_controller)
        append_button.append(button)

        Utilities.addButtonsToDB(append_button)

# NOTE: Remove Button Frame

    def removeButton(frame):

        Utilities.showButtonList(frame, "rm")

        Utilities.backButton(frame)

# NOTE: Modify Button Frame

    def modifyButtons(frame):

        Utilities.showButtonList(frame, "mod")

        Utilities.backButton(frame)

    def buttonDetails(frame, button_id):

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

        for item in entry_dict:

            def showItems(item):
                if not item[0:5] == "Label":
                    entry_dict[item].insert(0, "test " + item)

                return entry_dict[item].pack()

            showItems(item)

        current_data = Utilities.getButtonList()
        data_list = ["title", "domain", "username", "domain_controller"]
        button = [button for button in current_data if button.id == button_id]

        for items in entry_dict:
            if not items[0:5] == "Label":
                for item in data_list:

                    def test(items, item):
                        entry_dict[items].delete(0, END)
                        entry_dict[items].insert(0, button.item)

                    return entry_dict[items].pack()

        test(items, item)

        def getEntries(entry_dict=entry_dict):
            entry_data = {}
            for item in entry_dict:
                if not item[0:5] == "Label":
                    entry_data[item] = entry_dict[item].get()
            return entry_data

        # save_button = Button(
        #     frame,
        #     text="SAVE",
        #     command=lambda:
        #     [Utilities.saveButton(getEntries()),
        #      Utilities.mainFrame(frame)])
        # save_button.pack()

        Utilities.backButton(frame)

    def saveButton(entry_data):

        append_button = Utilities.getButtonList()

        new_title = entry_data["title"]
        new_domain = entry_data["domain"]
        new_username = entry_data["username"]
        new_domain_controller = entry_data["domain_controller"]

        # Generate a unique id for the button
        if append_button:
            max_id = max(button.id for button in append_button)
            button_id = max_id + 1
        else:
            button_id = 0

        button = Utilities(id=button_id,
                           root='',
                           title=new_title,
                           domain=new_domain,
                           username=new_username,
                           domain_controller=new_domain_controller)
        append_button.append(button)

        Utilities.addButtonsToDB(append_button)

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

    def addButtonsToDB(button_list):

        # Convert the list of buttons to JSON
        jsonStr = Utilities.listToJson(button_list)

        # Specify the filename where you want to save the JSON data
        filename = 'BD.json'

        # Open the file in write mode and save the JSON data
        with open(filename, 'w') as file:
            # Use indent=4 for pretty formatting
            json.dump(json.loads(jsonStr), file, indent=4)

        print(f'Saved {len(button_list)}th button to {filename}')

    def removeButtonFromDB(frame, button_id):
        filename = "BD.json"
        with open(filename, 'r') as f:
            data = json.load(f)

        data = [button for button in data if button['id'] != button_id]
        # Write the data back to the file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        Utilities.removeButton(frame)

    def modifyButtonFromDB(frame, button_id):

        filename = "BD.json"

        with open(filename, 'r') as f:
            data = json.load(f)

        buttonData = [button for button in data if button['id'] == button_id]

        print(buttonData)

        Utilities.modifyButtons(frame)

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

    def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def backButton(frame):

        exit_button = Button(frame,
                             text="FUCK GO BACK",
                             command=lambda: [Utilities.mainFrame(frame)])
        exit_button.pack()


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
#     Utilities.addButtonsToDB(button_list)
