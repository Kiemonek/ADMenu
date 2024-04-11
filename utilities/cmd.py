"""This module contains the CMDHandler class."""
import os


class CMD:
    """This class is used to run commands in the command prompt."""

    def __init__(self, button):
        self.button = button

    def connect_dsa(self, button):
        """This method is used to connect to the domain controller using the DSA snap-in."""
        command = f'runas /netonly /user:{button.domain}\\{button.username} "mmc dsa.msc /server={button.domain_controller}"'
        os.system(command)
