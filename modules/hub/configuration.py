#!/usr/bin/python
""" Configuration
Contains the Configuration object and methods used for loading and
manipulating configuration information.
"""

import xml.etree.ElementTree as ET

"""
    Recursively goes through the XML tree creating a dict object from the
    XML elements.
    Key = XML tag name
    Value = a dict of the child elements OR the text between the elements
"""
def _get_dict_from_xml(root):
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


    def _load_file(self):
        tree = ET.parse(self.config_file_name)
        root = tree.getroot()
        self.config_data = _get_dict_from_xml(root)
        print(self.config_data)
