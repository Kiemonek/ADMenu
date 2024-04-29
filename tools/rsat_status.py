"""This module is used to get the status of the RSAT feature."""
import ctypes
import os
import time
import tkinter as tk
from tkinter import messagebox
from utilities import constants
from utilities.resource_path import ResourcePath


class RsatStatus:
    """This class is used to get the status of the RSAT feature."""

    def __init__(self, frame):
        self.frame = frame

    def display_status(self, frame, status=None):
        """This method displays the status of the RSAT feature."""
        status = RsatStatus.get_status(self)
        if status == constants.RSAT_INSTALLATION:
            text = constants.RSAT_INSTALLATION
        else:
            text = constants.RSAT_STATUS + status

        button = tk.Button(
            frame,
            text=text,
            bg=constants.BTN_BG_CLR,
            fg=constants.BTN_FG_CLR,
            font=constants.BTN_FONT_DETAILS,
            activebackground=constants.BTN_ACTIVE_BG_CLR,
            borderwidth=0,
        )

        button.place(relwidth=0.35,
                     relheight=0.08,
                     anchor="n",
                     relx=0.85,
                     rely=0.0)

        if status == constants.RSAT_NOT_INSTALLED:
            button.config(command=lambda: RsatStatus.install_rsat(self))
        elif status == constants.RSAT_INSTALLED:
            button.config(state="disabled")
        else:
            button.config(
                command=lambda: RsatStatus.update_status(self, frame))

    def get_status(self):
        """This method gets the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self,
                                                  constants.RSATSTATUSFILENAME)

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            status_data = open(filename, "a", encoding="utf-8")
            status_data.write(constants.RSAT_UNKNOWN)
            status_data.close()

        status_data = open(filename, "r", encoding="utf-8")
        data = status_data.readlines()
        status_data.close()

        if constants.RSAT_NOT_INSTALLED in data:
            status = constants.RSAT_NOT_INSTALLED
        elif constants.RSAT_INSTALLED in data:
            status = constants.RSAT_INSTALLED
        elif constants.RSAT_INSTALLATION in data:
            status = constants.RSAT_INSTALLATION
        else:
            status = constants.RSAT_UNKNOWN

        return status

    def update_status(self, frame):
        """This method updates the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)

        cmd_command = 'powershell -Command'
        ps_command = 'Get-WindowsCapability -Name RSAT* -Online'
        format_command = 'Format-List -Property State'
        command_output = f"Out-File -FilePath '{filename}' -Encoding utf8"

        full_command = f'{cmd_command} "{ps_command} | {format_command} | {command_output}"'

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                                            f'/C {full_command}', None, 0)

        RsatStatus.status_updater(self, frame)

    def status_updater(self, frame):
        """This method gets the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            RsatStatus.update_status(self, frame)

            buffer = 0
            while not os.path.exists(filename) or os.path.getsize(
                    filename) == 0:
                time.sleep(0.5)
                buffer += 0.5
                if buffer == 10:
                    messagebox.showerror(
                        title="Error",
                        message="An error occurred while updating the status.")
                    break

        database = open(filename, "r", encoding="utf-8")
        data = database.readlines()
        database.close()

        status_list = []
        for line in data:
            if constants.RSAT_INSTALLED in line:
                status_list.append(constants.RSAT_INSTALLED)
            elif len(line) < 3 or line == "\n":
                pass
            else:
                status_list.append(constants.RSAT_NOT_INSTALLED)

        if constants.RSAT_NOT_INSTALLED in status_list and RsatStatus.get_status(
                self) == constants.RSAT_INSTALLATION:
            RsatStatus.write_status(self, constants.RSAT_INSTALLATION)
        elif constants.RSAT_NOT_INSTALLED in status_list:
            RsatStatus.write_status(self, constants.RSAT_NOT_INSTALLED)
        else:
            RsatStatus.write_status(self, constants.RSAT_INSTALLED)

        counter = status_list.count(constants.RSAT_INSTALLED)
        modules = len(status_list)

        messagebox.showinfo(
            title="RSAT Modules",
            message=f"RSAT modules installed: {counter}/{modules}")

        RsatStatus.display_status(self, frame)

    def install_rsat(self):
        """This method installs the RSAT feature."""
        cmd_command = 'powershell -Command'
        ps_command = 'Get-WindowsCapability -Name RSAT* -Online'
        install_command = 'Add-WindowsCapability -Online'

        full_command = f'{cmd_command} "{ps_command} | {install_command}"'

        def question(self):
            confirm = messagebox.askyesno(
                title="Install RSAT", message="Do you want to install RSAT?")

            if confirm:
                print(full_command)
                # ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                #                                     f'/C {full_command}', None, 0)

                RsatStatus.write_status(self, constants.RSAT_INSTALLATION)

        question(self)

    def write_status(self, text):
        """This method writes the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self,
                                                  constants.RSATSTATUSFILENAME)

        status = open(filename, "w", encoding="utf-8")
        status.write(text)
        status.close()
