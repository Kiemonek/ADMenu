"""This module contains the CMDHandler class."""
import os
import subprocess


class CMD:
    """Class to handle the command line arguments."""

    def __init__(self, button):
        """Initialize the CMDHandler class."""

        self.button = button

    def connect_dsa(self, button):
        """Connect to the DSA."""
        command = 'runas /netonly /user:' + button.domain + "\\" + button.username + ' "mmc dsa.msc /server=' + button.domain_controller + '" '

        subprocess.Popen(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        #   ,creationflags=subprocess.CREATE_NO_WINDOW)

        # stdout = stdout.read().decode('utf-8')
        # stderr = result.stderr.read().decode('utf-8')
        # print("Output:", stdout)
        # print("Error:", stderr)
