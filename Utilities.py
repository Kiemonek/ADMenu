import json
import os
from tkinter import *
import tkinter as tk
from tkinter.ttk import *


class Utilities:

    def __init__(self, id, root, title, domain, username, domain_controller):
        self.id = id
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

# NOTE: Main Frame

    def mainFrame(frame, bottomBar):

        Utilities.showButtonList(frame, "cmd")

        dsa_button = tk.Button(
            bottomBar,
            text="CONNECT",
            width=30,
            height=2,
            command=lambda: [Utilities.showButtonList(frame, "cmd")])
        dsa_button.place(anchor='se', relx=0.46, rely=0.45)

        add_button = tk.Button(
            bottomBar,
            text="ADD",
            width=30,
            height=2,
            command=lambda: [Utilities.buttonDetails(frame)])
        add_button.place(anchor='sw', relx=0.54, rely=0.45)

        mod_button = tk.Button(
            bottomBar,
            text="MODIFY",
            width=30,
            height=2,
            command=lambda: [Utilities.showButtonList(frame, "mod")])
        mod_button.place(anchor='ne', relx=0.46, rely=0.55)

        rem_button = tk.Button(
            bottomBar,
            text="REMOVE",
            width=30,
            height=2,
            command=lambda: [Utilities.showButtonList(frame, "rm")])
        rem_button.place(anchor='nw', relx=0.54, rely=0.55)

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

        jsonStr = Utilities.listToJson(button_list)
        filename = 'BD.json'

        with open(filename, 'w') as file:
            json.dump(json.loads(jsonStr), file, indent=4)

    def removeButtonFromDB(frame, button_id):
        filename = "BD.json"
        with open(filename, 'r') as f:
            data = json.load(f)

        data = [button for button in data if button['id'] != button_id]

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        Utilities.showButtonList(frame, "rm")


# NOTE: Utility Functions

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

        if option == "rm":
            text = "Choose and press button to remove"
        elif option == "mod":
            text = "Choose and press button to modify"
        elif option == "cmd":
            text = "Choose and press button to connect dsa"

        label = Label(frame, text=text)
        label.pack(side=TOP, fill=BOTH, expand=True)

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
        if button_id is None:
            text = "Add New Button"
        else:
            text = "Modify Button"

        label = Label(frame, text=text)
        label.pack(anchor=CENTER, fill=BOTH, expand=True)

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
                                 Utilities.mainFrame(frame)
                             ])
        save_button.pack()

    def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

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
