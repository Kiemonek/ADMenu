"""This module contains the class to configure the main window of the application."""
from app import constants


class WinConfig:
    """Class to configure the main window of the application."""

    def __init__(self, root, top_frame, bottom_frame):
        self.root = root
        self.top_frame = top_frame
        self.bottom_frame = bottom_frame

        self.root.title("AD Menu")
        self.root.geometry(
            f"{constants.WINDOW_WIDTH}x{constants.WINDOW_HEIGHT}")
        self.root.configure(background="#1E1E1E")
        self.root.resizable(False, False)

        self.top_frame.config(background="#838383")
        self.top_frame.place(relwidth=0.97,
                             relheight=0.84,
                             rely=0.02,
                             relx=0.5,
                             anchor="n")

        self.bottom_frame.config(background="#838383")
        self.bottom_frame.place(relwidth=0.97,
                                relheight=0.10,
                                rely=0.98,
                                relx=0.5,
                                anchor="s")
