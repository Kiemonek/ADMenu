"""This module is used to install the RSAT modules."""
import ctypes
from tkinter import messagebox
from command_executer.write_status import WriteStatus
from utilities import constants


class InstallRsat:
    """This class is used to install the RSAT modules."""

    def install_rsat(self):
        """This method installs the RSAT modules."""

        full_command = f'{constants.CMD_COMMAND} "{constants.PS_COMMAND}{constants.INSTALL_COMMAND}"'

        def question(self):
            confirm = messagebox.askyesno(title=constants.RSAT_ASK_TITLE,
                                          message=constants.RSAT_ASK_MESSAGE)

            if confirm:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe",
                                                    f'/C {full_command}', None,
                                                    0)

                WriteStatus.write_status(self, constants.RSAT_INSTALLATION)

        question(self)
