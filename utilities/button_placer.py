""" This module is used to place buttons on the frame. """


class ButtonPlacer:
    """This class is used to place buttons on the frame."""

    def __init__(self, button, id_button):
        self.button = button
        self.id_button = id_button

    def place_buttons(self, button, id_button):
        """This method is used to place buttons on the frame."""
        rel_x = (id_button % 5) + 1
        return button.place(relwidth=0.15,
                            height=40,
                            relx=rel_x,
                            rely=0.1 + (float(id_button) / 10))
