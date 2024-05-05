"""This module is used to write the status of the RSAT modules."""
from utilities import constants
from utilities.resource_path import ResourcePath


class WriteStatus:
    """This class is used to write the status of the RSAT modules."""

    def write_status(self, text):
        """This method writes the status of the RSAT modules."""
        filename = ResourcePath.get_resource_path(self,
                                                  constants.RSATSTATUSFILENAME)

        status = open(filename, "w", encoding="utf-8")
        status.write(text)
        status.close()
