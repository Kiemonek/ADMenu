"""This module is used to get the status of the RSAT feature."""
import ctypes
import os
import tkinter as tk
from utilities import constants
from utilities.resource_path import ResourcePath


class RsatStatus:
    """This class is used to get the status of the RSAT feature."""

    def __init__(self, frame):
        self.frame = frame

    def display_status(self, frame, status=None):
        """This method displays the status of the RSAT feature."""
        text = constants.RSAT_STATUS
        rel_x = 0.85
        rel_y = 0.0

        if status == constants.RSAT_INSTALLED:
            text += constants.RSAT_INSTALLED
        elif status == constants.RSAT_NOT_INSTALLED:
            text += constants.RSAT_NOT_INSTALLED
        else:
            text += constants.RSAT_IDK

        button = tk.Button(frame,
                           text=text,
                           bg=constants.BTN_BG_CLR,
                           fg=constants.BTN_FG_CLR,
                           font=constants.BTN_FONT_DETAILS,
                           activebackground=constants.BTN_ACTIVE_BG_CLR,
                           command=lambda: RsatStatus.update_status(self))

        button.place(relwidth=0.25,
                     relheight=0.08,
                     anchor="n",
                     relx=rel_x,
                     rely=rel_y)

    def get_status(self):
        """This method gets the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)
        valid_statuses = [
            constants.RSAT_IDK, constants.RSAT_INSTALLED,
            constants.RSAT_NOT_INSTALLED
        ]
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            RsatStatus.update_status(self)

        else:
            database = open(filename, "r", encoding="utf-8")
            status = database.read()
            database.close()

        if status not in valid_statuses:
            status = constants.RSAT_IDK

        return status

    def update_status(self):
        """This method updates the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)

        cmd_command = 'powershell -Command'
        ps_command = 'Get-WindowsCapability -Name RSAT* -Online'
        format_command = 'Format-List -Property State'
        command_output = f"Out-File -FilePath '{filename}' -Encoding utf8"

        full_command = f'{cmd_command} "{ps_command} | {format_command} | {command_output}"'

        print(full_command)

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                                            f'/C {full_command}', None, 0)

        return True

    def install_rsat(self):
        return True
