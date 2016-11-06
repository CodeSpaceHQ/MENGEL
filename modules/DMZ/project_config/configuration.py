#!/usr/bin/python
""" Configuration
Contains the Configuration object and methods used for loading and
manipulating configuration information.
"""

import xml.etree.ElementTree as ET

"""
The list below contains the values of the required XML tags that should be
in the configuration XML file. If any one of these is not in the XML file, an
error will be thrown.
"""
TAG_ROOT = "MLTF-Configuration"
REQUIRED_TAGS = ["Project-Name", "User-Name", "Firebase", \
"Files", "Prediction", "Models"]


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ConfigurationError(Exception):
    """Generic error for exceptions created in this module."""
    def __init__(self, message):
        super(ConfigurationError, self).__init__(message)
        self.message = message


class Configuration(object):
    """
    Holds all data and methods for manipulating data found in the configuration xml file.
    Will also handle saving data back to xml once done.
    """
    def __init__(self, config_file_name):
        super(Configuration, self).__init__()
        self.config_file_name = config_file_name
        self.config_data = {}
        self._load_file()

    def _load_file(self):
        """ Loads the XML file and checks root tag for validaty"""
        self.tree = ET.parse(self.config_file_name)
        self.root = self.tree.getroot()
        if not self.root.tag == TAG_ROOT:
            raise ConfigurationError('Required XML root tag [{}] not found in\
             {}'.format(TAG_ROOT, self.config_file_name))

        self.project_name = self.root.attrib.get("name")
        self.user_name = self.root.attrib.get("user")
