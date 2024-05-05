"""This module is used to get the status of the RSAT modules."""
import os
from utilities import constants
from utilities.resource_path import ResourcePath


class GetStatus:
    """This class is used to get the status of the RSAT modules."""

    def get_status(self):
        """This method gets the status of the RSAT modules."""
        filename = ResourcePath.get_resource_path(self,
                                                  constants.RSATSTATUSFILENAME)

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            status_data = open(filename, "a", encoding="utf-8")
            status_data.write(constants.RSAT_UNKNOWN)
            status_data.close()

        status_data = open(filename, "r", encoding="utf-8")
        data = status_data.readlines()
        status_data.close()

        if constants.RSAT_NOT_INSTALLED in data:
            status = constants.RSAT_NOT_INSTALLED
        elif constants.RSAT_INSTALLED in data:
            status = constants.RSAT_INSTALLED
        elif constants.RSAT_INSTALLATION in data:
            status = constants.RSAT_INSTALLATION
        else:
            status = constants.RSAT_UNKNOWN

        return status
