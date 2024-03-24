"""This module is used to show the buttons in the main frame."""
import tkinter as tk
import app.constants as constants
from utilities.label_creator import LabelCreator
from utilities.clear_frame import ClearFrame
from utilities.button_creator import ButtonCreator
from database.json_helpers import JsonHelpers
from buttons.save_button import SaveButton
from buttons.get_buttons import GetButtons


class TopBar:
    """This class is used to show the buttons in the main frame."""

    def __init__(self, buttons):
        self.buttons = buttons

    def show_button_list(self, frame, option):
        """This method creates the button list frame. It is used to remove, modify or connect."""
        ClearFrame.clear_frame(self, frame)
        ClearFrame.clear_frame(self, frame)

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

        button_list = GetButtons.get_button_list(self)
        button_list = GetButtons.get_button_list(self)
        for items in button_list:

            def on_pressed(items):
                """This method creates buttons with different commands depending on the option selected."""
                if option == "rm":
                    return lambda: [
                        JsonHelpers.remove_button_from_db(
                            self, items.id_button),
                        TopBar.show_button_list(self, frame, "rm")
                    ]
                elif option == "mod":
                    return TopBar.button_details(self, frame, items.id_button)

                elif option == "cmd":
                    return print('runas /netonly /user:' + items.domain +
                                 "\\" + items.username +
                                 ' "mmc dsa.msc /server=' +
                                 items.domain_controller + '" ')

            button = tk.Button(frame,
                               text=items.title,
                               command=on_pressed(items))
            button.place(width=80,
                         height=40,
                         relx=0.5,
                         rely=0.1 + (float(items.id_button) / 10))

    def button_details(self, top_frame, button_id=None):
        """This method creates the buttun top_frame. It is used to add or modify a button."""
        ClearFrame.clear_frame(self, top_frame)
        if button_id is None:
            text = "Add New Button"
        else:
            text = "Modify Button"

        label = tk.Label(top_frame,
                         text=text,
                         fg=constants.TOP_LBL_FG_CLR,
                         bg=constants.TOP_LBL_BG_CLR,
                         font=constants.FONT_DETAILS)
        label.place(relwidth=1, relheight=0.1, relx=0.5, anchor="n")

        #FIXME: This is not working
        label_name = LabelCreator.create_label(self, top_frame, "Name:"),
        label_domain = LabelCreator.create_label(self, top_frame, "Domain:"),
        label_username = LabelCreator.create_label(self, top_frame,
                                                   "Username:"),
        label_domain_controller = LabelCreator.create_label(
            self, top_frame, "Controller:"),

        entry_dict = {}
        entry_dict.update({"LabelName": label_name})

        # entry_dict = {
        #     "LabelName":
        #     LabelCreator.create_label(self, top_frame, text="Name:"),
        #     "title":
        #     Entry(top_frame),
        #     "LabelDomain":
        #     Label(top_frame,
        #           text="Domain:",
        #           fg=cons.CONTENT_FG_CLR,
        #           bg=cons.CONTENT_BG_CLR,
        #           font=cons.FONT_DETAILS),
        #     "domain":
        #     Entry(top_frame),
        #     "LabelUsername":
        #     Label(top_frame,
        #           text="Username:",
        #           fg=cons.CONTENT_FG_CLR,
        #           bg=cons.CONTENT_BG_CLR,
        #           font=cons.FONT_DETAILS),
        #     "username":
        #     Entry(top_frame),
        #     "LabelServer":
        #     Label(top_frame,
        #           text="Domain Controller:",
        #           fg=cons.CONTENT_FG_CLR,
        #           bg=cons.CONTENT_BG_CLR,
        #           font=cons.FONT_DETAILS),
        #     "domain_controller":
        #     Entry(top_frame),
        # }
        if button_id is None:
            entry_dict["title"].insert(0, "Company A")
            entry_dict["domain"].insert(0, "companya.com")
            entry_dict["username"].insert(0, "user1")
            entry_dict["domain_controller"].insert(0, "192.168.21.37")
        else:
            current_data = GetButtons.get_button_list(self)
            current_data = GetButtons.get_button_list(self)
            for items in current_data:
                if items.id_button == button_id:
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

        entry_dict["LabelName"].place(relx=0.1, rely=0.2)
        entry_dict["title"].place(relx=0.5, rely=0.2)
        entry_dict["LabelDomain"].place(relx=0.1, rely=0.35)
        entry_dict["domain"].place(relx=0.5, rely=0.35)
        entry_dict["LabelUsername"].place(relx=0.1, rely=0.5)
        entry_dict["username"].place(relx=0.5, rely=0.5)
        entry_dict["LabelServer"].place(relx=0.1, rely=0.65)
        entry_dict["domain_controller"].place(relx=0.5, rely=0.65)

        def get_entries(entry_dict):
            entry_data = {}
            for item in entry_dict:
                if not item[0:5] == "Label":
                    entry_data[item] = entry_dict[item].get()

            return entry_data

        button_id = button_id if button_id is not None else None
        save_button = ButtonCreator.create_button(
            self, top_frame, "SAVE", lambda: [
                SaveButton.save_button(top_frame, get_entries(entry_dict),
                                       button_id),
                TopBar.button_details(self, top_frame)
            ])
        save_button.place(relx=0.5,
                          rely=0.85,
                          relwidth=0.25,
                          relheight=0.08,
                          anchor="n")
