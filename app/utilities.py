"""A module for the utilities of the application."""
import json
# import os
import tkinter as tk


class Utilities:
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

    def getButtonList():
        filename = "BD.json"
        database = open(filename, "r")
        data = json.loads(database.read())

        button_list = []
        for item in data:
            button = Utilities(id_button=item['id_button'],
                               root=None,
                               title=item['title'],
                               domain=item['domain'],
                               username=item['username'],
                               domain_controller=item['domain_controller'])
            button_list.append(button)
        database.close()
        return button_list

    def show_button_list(self, frame, option):

        Utilities.clear_frame(frame)

        if option == "rm":
            text = "Choose and press button to remove"
        elif option == "mod":
            text = "Choose and press button to modify"
        elif option == "cmd":
            text = "Choose and press button to connect dsa"

        label = tk.Label(frame,
                         text=text,
                         fg='#838383',
                         bg='#1E1E1E',
                         font=("Microsoft YaHei", 12, "bold"))
        label.place(relwidth=1, relheight=0.1, relx=0.5, anchor="n")

        button_list = Utilities.getButtonList()
        for items in button_list:

            def on_pressed(x=items):
                if option == "rm":
                    return Utilities.removeButtonFromDB(frame, x.id_button)
                elif option == "mod":
                    return Utilities.buttonDetails(frame, x.id_button)
                elif option == "cmd":
                    print('runas /netonly /user:' + x.domain + "\\" +
                          x.username + ' "mmc dsa.msc /server=' +
                          x.domain_controller + '" ')
                else:
                    print("Error: Option not found")

            button = tk.Button(
                frame,
                text=items.title,
                command=onPressed,
            )
            button.place(width=80,
                         height=40,
                         relx=0.5,
                         rely=0.1 + (float(items.id_button) / 10))

        def get_entries(entry_dict):
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
                                 Utilities.main_frame(frame)
                             ])
        save_button.place()

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def save_button(self, entry_data, button_id=None):
        if button_id is None:
            append_button = Utilities.getButtonList()
        else:
            current_data = Utilities.getButtonList()
            append_button = [
                button for button in current_data
                if not button.id_button == button_id
            ]

        new_title = entry_data["title"]
        new_domain = entry_data["domain"]
        new_username = entry_data["username"]
        new_domain_controller = entry_data["domain_controller"]

        # Generate a unique id_button for the button
        if button_id is None:
            max_id = max(button.id_button for button in append_button)
            button_id = max_id + 1
        elif button_id is not None:
            button_id = button_id
        else:
            button_id = 0

        button = Utilities(id_button=button_id,
                           root='',
                           title=new_title,
                           domain=new_domain,
                           username=new_username,
                           domain_controller=new_domain_controller)
        append_button.append(button)
        append_button = sorted(append_button, key=lambda x: x.id_button)

        Utilities.saveChangesToDB(append_button)
