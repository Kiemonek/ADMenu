"""This module is used to buffer the status of the file."""
import os
import time
from tkinter import messagebox

from utilities import constants


class Buffer:
    """This class is used to buffer the status of the file."""

    def __init__(self, filename):
        self.buffer = constants.BUFFER_START
        self.filename = filename

        while not os.path.exists(filename) or os.path.getsize(filename) == 0:

            time.sleep(constants.BUFFER_SLEEP)
            self.buffer += constants.BUFFER_SLEEP

            if self.buffer == constants.BUFFER_FINISH:
                messagebox.showerror(
                    title=constants.BUFFER_TITLE,
                    message=constants.BUFFER_MESSAGE,
                )
                break
