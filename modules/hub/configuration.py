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
tag_root = "MLTF-Configuration"
required_tags = ["Project-Name","User-Name","Firebase",\
"Files","Prediction","Models"]


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ConfigurationError(Exception):
    """Generic error for exceptions created in this module."""
    def __init__(self, message):
        super(ConfigurationError,self).__init__(message)
        self.message = message

def _get_dict_from_xml(root):
    """
    Recursively goes through the XML tree creating a dict object from the
    XML elements.
    Key = XML tag name
    Value = a dict of the child elements OR the text between the elements
    """
    result = {}
    if len(list(root)) == 0:
        result[root.tag] = root.text.rstrip().strip()
        return result
    for child in root:
        result[child.tag] = _get_dict_from_xml(child)
    return result

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
        self._validate_loaded_dict()


    def _load_file(self):
        """ Loads the XML file and checks root tag for validaty"""
        tree = ET.parse(self.config_file_name)
        root = tree.getroot()
        if not root.tag == tag_root:
            raise ConfigurationError('Required XML root tag [{}] not found in {}'.format(tag_root,self.config_file_name))

        self.config_data = _get_dict_from_xml(root)

    def _validate_loaded_dict(self):
        """ Checks to make sure all required tags are in the loaded dictionary from the XML file """
        for tag in required_tags:
            if not self.config_data.has_key(tag):
                raise ConfigurationError('Required XML tag [{}] not found in {}'.format(tag,self.config_file_name))
