"""This module is used to get the status of the RSAT feature."""
import ctypes
import os
import time
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
                           borderwidth=0,
                           command=lambda: RsatStatus.get_status(self, frame))

        button.place(relwidth=0.25,
                     relheight=0.08,
                     anchor="n",
                     relx=rel_x,
                     rely=rel_y)

    def get_status(self, frame):
        """This method gets the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            RsatStatus.update_status(self)

            buffer = 0
            while not os.path.exists(filename) or os.path.getsize(
                    filename) == 0:
                time.sleep(0.5)
                buffer += 0.5
                if buffer == 10:
                    print("Error: File not found or empty.")
                    break

        database = open(filename, "r", encoding="utf-8")
        data = database.readlines()
        database.close()

        status_list = []
        for line in data:
            if constants.RSAT_INSTALLED in line:
                status_list.append(constants.RSAT_INSTALLED)
            elif len(line) < 3 or line == "\n":
                #TODO: change it go not contain "State :"
                pass
            else:
                status_list.append(constants.RSAT_NOT_INSTALLED)

        if constants.RSAT_NOT_INSTALLED in status_list:
            RsatStatus.display_status(self, frame,
                                      constants.RSAT_NOT_INSTALLED)
        else:
            RsatStatus.display_status(self, frame, constants.RSAT_INSTALLED)

    def update_status(self):
        """This method updates the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)

        cmd_command = 'powershell -Command'
        ps_command = 'Get-WindowsCapability -Name RSAT* -Online'
        format_command = 'Format-List -Property State'
        command_output = f"Out-File -FilePath '{filename}' -Encoding utf8"

        full_command = f'{cmd_command} "{ps_command} | {format_command} | {command_output}"'

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                                            f'/C {full_command}', None, 0)

    def install_rsat(self):
        """This method installs the RSAT feature."""
        cmd_command = 'powershell -Command'
        ps_command = 'Get-WindowsCapability -Name RSAT* -Online'
        install_command = 'Add-WindowsCapability -Online -Name'

        full_command = f'{cmd_command} "{ps_command} | {install_command}"'

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                                            f'/C {full_command}', None, 0)
        rem_command = f'del "{ResourcePath.get_resource_path(self, constants.RSATFILENAME)}"'

        #TODO: Test output on a VM


#TODO: RSAT Status based on other file
