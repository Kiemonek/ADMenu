"""This module contains the CMDHandler class."""
import os
import sys
import ctypes

class DSAConnect:
    """This class is used to run commands in the command prompt."""

    def __init__(self, button):
        self.button = button

    def connect_dsa(self, button):
        """This method is used to connect to the domain controller using the DSA snap-in."""
        domain_user = f'{button.domain}\\{button.username}'
        mmc_command = f'mmc dsa.msc /server={button.domain_controller}'
        full_command = f'cmd.exe /C runas /netonly /user:{domain_user} "{mmc_command}"'

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f'/C {full_command}', None, 1)

            