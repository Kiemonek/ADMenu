"""This module is used to show the buttons in the main frame."""
import tkinter as tk
from app.button_details import ButtonDetails as dt
from app.json_helpers import JsonHelpers as jh
from app.get_buttons import GetButtons as gb
from app.clear_frame import ClearFrame as cf


class ShowButtons:
    """This class is used to show the buttons in the main frame."""

    def __init__(self, buttons):
        self.buttons = buttons

    def show_button_list(self, frame, option):
        """This method creates the button list frame. It is used to remove, modify or connect."""
        cf.clear_frame(self, frame)

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

        button_list = gb.get_button_list(self)
        for items in button_list:

            def on_pressed(x=items):
                if option == "rm":
                    return tk.Button(
                        frame,
                        text=x.title,
                        command=lambda: [
                            jh.remove_button_from_db(self, x.id_button),
                            ShowButtons.show_button_list(self, frame, "rm")
                        ],
                    )
                elif option == "mod":
                    return tk.Button(
                        frame,
                        text=x.title,
                        command=lambda: [
                            dt.button_details(self, frame, x.id_button)
                            #FIXME: This is not working
                            # , ShowButtons.show_button_list(self, frame, "mod")
                        ],
                    )
                elif option == "cmd":
                    return tk.Button(
                        frame,
                        text=x.title,
                        command=lambda: [
                            print('runas /netonly /user:' + x.domain + "\\" + x
                                  .username + ' "mmc dsa.msc /server=' + x.
                                  domain_controller + '" ')
                        ],
                    )
                else:
                    print("Error: Option not found")

            button = on_pressed(items)
            button.place(width=80,
                         height=40,
                         relx=0.5,
                         rely=0.1 + (float(items.id_button) / 10))
