import json
import os
from tkinter import *
from tkinter.ttk import *


class DashboardButton:
    # Button dashboard initializer
    def __init__(self, id, root, title, domain, username, domain_controller):
        self.id = id
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
        # Create a list of DashboardButton instances from the dictionaries
        button_list = []
        for button_dict in json_button_list:
            button = DashboardButton(
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
        # Create a new DashboardButton instance using the dictionary values
        return cls(id=button_dict["id"],
                   root=None,
                   title=button_dict["title"],
                   domain=button_dict["domain"],
                   username=button_dict["username"],
                   domain_controller=button_dict["domain_controller"])

    # Return list of available buttons
    def getButtonList():
        filename = "BD.json"
        database = open(filename, "r")
        data = json.loads(database.read())

        button_list = []
        for item in data:
            button = DashboardButton(
                id=item['id'],
                root=None,
                title=item['title'],
                domain=item['domain'],
                username=item['username'],
                domain_controller=item['domain_controller'])
            button_list.append(button)
        database.close()
        return button_list

    def addButtonsToDB(button_list):

        # Convert the list of buttons to JSON
        jsonStr = DashboardButton.listToJson(button_list)

        # Specify the filename where you want to save the JSON data
        filename = 'BD.json'

        # Open the file in write mode and save the JSON data
        with open(filename, 'w') as file:
            # Use indent=4 for pretty formatting
            json.dump(json.loads(jsonStr), file, indent=4)

        print(f'Saved {len(button_list)}th button to {filename}')

    def removeButtonFromDB(button_id):

        filename = "BD.json"

        # Load the existing data
        with open(filename, 'r') as f:
            data = json.load(f)

        # Remove the button with the given id
        data = [button for button in data if button['id'] != button_id]

        # Write the data back to the file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        print(f'Removed button with id {button_id}')

    def modifyButtonFromDB(button_id):

        filename = "BD.json"

        with open(filename, 'r') as f:
            data = json.load(f)

        buttonData = [button for button in data if button['id'] == button_id]

        print(buttonData)

    # Returning command class for buttons
    def onPressed(self, option):
        if option == "cmd":
            print('runas /netonly /user:' + self.domain + "\\" +
                  self.username + ' "mmc dsa.msc /server=' +
                  self.domain_controller + '" ')
        elif option == "rm":
            DashboardButton.removeButtonFromDB(self.id)
        elif option == "mod":
            DashboardButton.modifyButtonFromDB(self.id)
        else:
            print("Error: Option not found")

# NOTE: Main Frame

    def mainFrame(frame):

        DashboardButton.showButtonList(frame, "cmd")

        # Usable Buttons
        add_button = Button(
            frame,
            text="Add New Button",
            command=lambda: [DashboardButton.addNewButton(frame)])
        add_button.grid()
        mod_button = Button(
            frame,
            text="Modify Buttons",
            command=lambda: [DashboardButton.modifyButtons(frame)])
        mod_button.grid()
        rem_button = Button(
            frame,
            text="Remove Button",
            command=lambda: [DashboardButton.removeButton(frame)])
        rem_button.grid()

# NOTE: Add Button Window

    def addNewButton(frame):

        DashboardButton.clear_frame(frame)

        label = Label(frame, text="Insert data")
        label.grid()

        label_name = Label(frame, text="Name:")
        label_name.grid()

        entry_name = Entry(frame)
        entry_name.insert(0, "test name")
        entry_name.grid()

        label_domain = Label(frame, text="Domain:")
        label_domain.grid()

        entry_domain = Entry(frame)
        entry_domain.insert(0, "test domain")
        entry_domain.grid()

        label_username = Label(frame, text="Username:")
        label_username.grid()

        entry_username = Entry(frame)
        entry_username.insert(0, "login")
        entry_username.grid()

        label_server = Label(frame, text="Server:")
        label_server.grid()

        entry_first_octet = Entry(frame)
        entry_first_octet.insert(0, "111")
        entry_first_octet.grid()

        label_dot = Label(frame, text=".")
        label_dot.grid()

        entry_second_octet = Entry(frame)
        entry_second_octet.insert(0, "222")
        entry_second_octet.grid()

        label_dot = Label(frame, text=".")
        label_dot.grid()

        entry_third_octet = Entry(frame)
        entry_third_octet.insert(0, "333")
        entry_third_octet.grid()

        label_dot = Label(frame, text=".")
        label_dot.grid()

        entry_fourth_octet = Entry(frame)
        entry_fourth_octet.insert(0, "444")
        entry_fourth_octet.grid()

        save_button = Button(frame,
                             text="SAVE",
                             command=lambda: [
                                 DashboardButton.saveAddedButton(
                                     entry_name, entry_domain, entry_username,
                                     entry_first_octet, entry_second_octet,
                                     entry_third_octet, entry_fourth_octet),
                                 DashboardButton.mainFrame(frame)
                             ])
        save_button.grid()

        DashboardButton.backButton(frame)

    def saveAddedButton(entry_name, entry_domain, entry_username,
                        entry_first_octet, entry_second_octet,
                        entry_third_octet, entry_fourth_octet):

        append_button = DashboardButton.getButtonList()

        new_title = entry_name.get()
        new_domain = entry_domain.get()
        new_username = entry_username.get()
        new_domain_controller = entry_first_octet.get(
        ) + "." + entry_second_octet.get() + "." + entry_third_octet.get(
        ) + "." + entry_fourth_octet.get()

        # Generate a unique id for the button
        if append_button:
            max_id = max(button.id for button in append_button)
            button_id = max_id + 1
        else:
            button_id = 0

        button = DashboardButton(id=button_id,
                                 root='',
                                 title=new_title,
                                 domain=new_domain,
                                 username=new_username,
                                 domain_controller=new_domain_controller)
        append_button.append(button)

        DashboardButton.addButtonsToDB(append_button)

# NOTE: Remove Button Window

    def removeButton(frame):

        DashboardButton.showButtonList(frame, "rm")

        DashboardButton.backButton(frame)

# NOTE: Modify Button Window

    def modifyButtons(frame):

        DashboardButton.showButtonList(frame, "mod")

        DashboardButton.backButton(frame)

# NOTE: Utility Functions

    def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def showButtonList(frame, option):
        DashboardButton.clear_frame(frame)
        # Implement list from json
        buttonList = DashboardButton.getButtonList()

        # Button Generator
        for items in buttonList:
            if option == "rm":
                button = Button(frame,
                                text=items.title,
                                command=lambda: [
                                    items.onPressed(option),
                                    DashboardButton.removeButton(frame)
                                ])
                button.grid()
            else:
                button = Button(frame,
                                text=items.title,
                                command=lambda: [items.onPressed(option)])
                button.grid()

    def backButton(frame):

        exit_button = Button(
            frame,
            text="FUCK GO BACK",
            command=lambda: [DashboardButton.mainFrame(frame)])
        exit_button.grid()


# This code will create a list of 10 buttons, convert them to JSON, and save them to a file named file.json.
# Create a list of 10 buttons
# button_list = []  # Define the button_list variable
# for i in range(1, 11):
#     button = DashboardButton(
#         id=i,
#         root='',  # You can set root to an appropriate value
#         title=f'My Button {i}',
#         domain=f'Domain {i}',
#         username=f'User {i}',
#         domain_controller=f'Controller {i}'
#     )
#     print(button.title)
#     button_list.append(button)
#     DashboardButton.addButtonsToDB(button_list)
