"""This module provides a class that fills an entry with a value."""
from database import constants
from buttons.get_buttons import GetButtons


class EntryFiller:
    """A class to represent the entry filler."""

    def __init__(self, entry_dict, button_id):
        self.entry_dict = entry_dict
        self.button_id = button_id

    def fill_entry(self, entry_dict, button_id=None):
        """This method fills an entry with a value."""

        button_data = {
            "title": constants.EXMPL_TITLE,
            "domain": constants.EXMPL_DOMAIN,
            "username": constants.EXMPL_USERNAME,
            "domain_controller": constants.EXMPL_DOMAIN_CONTROLLER,
        }

        if button_id is not None:
            current_data = GetButtons.get_button_list(self)
            for items in current_data:
                if items.id_button == button_id:
                    update_data = {
                        "title": items.title,
                        "domain": items.domain,
                        "username": items.username,
                        "domain_controller": items.domain_controller,
                    }
                    button_data.update(update_data)

        for key, value in button_data.items():

            entry = entry_dict.get(key)
            entry.insert(0, value)
