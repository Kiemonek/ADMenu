"""A module for the utilities of the application."""
from buttons.get_buttons import GetButtons
from database.json_helpers import JsonHelpers


class SaveButton:
    """A class to represent the utilities of the application."""

    def __init__(self, id_button, root, title, domain, username,
                 domain_controller):
        self.id_button = id_button
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller

    def save_button(self, entry_data, button_id=None):
        """This method saves the button to the database."""
        current_data = GetButtons.get_button_list(self)

        new_button = SaveButton(
            id_button=0,
            root='',
            title=entry_data["title"],
            domain=entry_data["domain"],
            username=entry_data["username"],
            domain_controller=entry_data["domain_controller"])

        if not current_data:
            append_button = [new_button]
        elif button_id is None:
            append_button = current_data
            max_id = max(button.id_button for button in append_button)
            new_button.id_button = max_id + 1
            append_button.append(new_button)
        else:
            new_button.id_button = button_id
            append_button = [
                button if not button.id_button == button_id else new_button
                for button in current_data
            ]

        append_button = sorted(append_button, key=lambda x: x.id_button)

        for i, button in enumerate(append_button):
            button.id_button = i

        JsonHelpers.save_changes_to_db(self, button_list=append_button)
