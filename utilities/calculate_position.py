""" This module is used to place buttons on the frame. """


class CalculatePosition:
    """This class is used to place buttons on the frame."""

    def __init__(self, id_button):
        self.id_button = id_button

    def calculate_rel_x(self, id_button):
        """This method calculates the relative x position of the button."""
        if id_button % 6 == 0:
            rel_x = 0.005
        else:
            rel_x = 0.005 + 0.165 * (id_button % 6)

        return rel_x

    def calculate_rel_y(self, id_button):
        """This method calculates the relative y position of the button."""
        if not id_button % 7 == 0 and id_button < 6 or id_button == 0:
            rel_y = 0.117
        else:
            rel_y = 0.117 + 0.11 * (id_button // 6 if id_button != 6 else 1)

        return rel_y
