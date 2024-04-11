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
        #FIXME: This method is not working as expected.
        current_data = GetButtons.get_button_list(self)

        if not current_data:

            append_button = []
            button_id = 0

        elif button_id is None:

            append_button = current_data

        else:
            append_button = [
                button for button in current_data
                if not button.id_button == button_id
            ]

            for i, button in enumerate(append_button):
                button.id_button = i

        if button_id is None:
            max_id = max(button.id_button for button in append_button)
            button_id = max_id + 1
        else:
            pass

        new_title = entry_data["title"]
        new_domain = entry_data["domain"]
        new_username = entry_data["username"]
        new_domain_controller = entry_data["domain_controller"]

        button = SaveButton(id_button=button_id,
                            root='',
                            title=new_title,
                            domain=new_domain,
                            username=new_username,
                            domain_controller=new_domain_controller)
        append_button.append(button)

        append_button = sorted(append_button, key=lambda x: x.id_button)
        JsonHelpers.save_changes_to_db(self, button_list=append_button)
