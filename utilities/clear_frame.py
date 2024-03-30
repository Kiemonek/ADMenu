"""This module is responsible for clearing the frame."""


class ClearFrame:
    """This class is responsible for clearing the frame."""

    def __init__(self, frame):
        self.frame = frame

    def clear_frame(self, frame):
        """This method clears the frame."""
        for widgets in frame.winfo_children():
            widgets.destroy()
