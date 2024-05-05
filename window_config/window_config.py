"""This module contains the class to configure the main window of the application."""
# import os
# import sys
import utilities.constants as constants
from utilities.resource_path import ResourcePath


class WinConfig:
    """Class to configure the main window of the application."""

    def __init__(self, root, top_frame, bottom_frame):
        self.root = root
        self.top_frame = top_frame
        self.bottom_frame = bottom_frame

        self.root.title(constants.WINDOW_TITLE)
        self.root.geometry(
            f"{constants.WINDOW_WIDTH}x{constants.WINDOW_HEIGHT}")
        self.root.configure(background=constants.WINDOW_BG_CLR)
        self.root.resizable(constants.WINDOW_HEIGHT, constants.WIDTH_RESIZABLE)
        icon=ResourcePath.resource_path(self, constants.ASSET_ICON)
        self.root.iconbitmap(icon)

        self.top_frame.config(background=constants.BAR_BG_CLR)
        self.top_frame.place(relwidth=0.97,
                             relheight=0.84,
                             rely=0.02,
                             relx=0.5,
                             anchor="n")

        self.bottom_frame.config(background=constants.BAR_BG_CLR)
        self.bottom_frame.place(relwidth=0.97,
                                relheight=0.10,
                                rely=0.98,
                                relx=0.5,
                                anchor="s")
