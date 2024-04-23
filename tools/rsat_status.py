"""This module is used to get the status of the RSAT feature."""
import ctypes
import os
from buttons.create_button import ButtonCreator
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

        ButtonCreator.create_button(
            self,
            frame,
            text,
            command=lambda: RsatStatus.update_status(self),
            rel_x=rel_x,
            rel_y=rel_y)

    def get_status(self):
        """This method gets the status of the RSAT feature."""
        filename = ResourcePath.get_resource_path(self, constants.RSATFILENAME)
        valid_statuses = [
            constants.RSAT_IDK, constants.RSAT_INSTALLED,
            constants.RSAT_NOT_INSTALLED
        ]
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            database = open(filename, "a", encoding="utf-8")
            database.write(constants.RSAT_IDK)
            database.close()
            status = constants.RSAT_IDK

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
        format_command = 'Format-List -Property State'  #DisplayName, State'
        command_output = f"Out-File -FilePath '{filename}' -Encoding utf8"

        full_command = f'{cmd_command} "{ps_command} | {format_command} | {command_output}"'

        print(full_command)

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                                            f'/C {full_command}', None, 1)

        return True

    def install_rsat(self):
        return True
