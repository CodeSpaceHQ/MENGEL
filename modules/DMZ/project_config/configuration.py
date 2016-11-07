#!/usr/bin/python
""" Configuration
Contains the Configuration object and methods used for loading and
manipulating configuration information.
"""

import xml.etree.ElementTree as ET
from model import Model

TAG_ROOT = 'MLTF-Configuration'
TAG_FILES = 'Files'
TAG_MODELS = 'Models'

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
    # pylint: disable=too-many-instance-attributes
    # nine is reasonable in this case.
    def __init__(self, config_file_name):
        super(Configuration, self).__init__()
        self.config_file_name = config_file_name
        self.config_data = {}
        self.models = {}
        self.test_files = []
        self.train_files = []
        self._load_file()


    def _load_file(self):
        """ Loads the XML file and checks root tag for validaty"""
        self.tree = ET.parse(self.config_file_name)
        self.root = self.tree.getroot()
        if not self.root.tag == TAG_ROOT:
            raise ConfigurationError('Required XML root tag [{}] not found in\
             {}'.format(TAG_ROOT, self.config_file_name))

        self.project_name = self.root.attrib.get('name', '')
        self.user_name = self.root.attrib.get('user', '')

        for child in self.root:
            if child.tag == TAG_MODELS:
                self._load_models(child)
            elif child.tag == TAG_FILES:
                self._load_files(child)
            else:
                self.config_data[child.tag] = child.attrib




    def _load_models(self, root):
        """
        Assumes the root is the <Models> XMl tag. Creates models from all
        the sub elements and adds them to the model dictionary where the key is
        the name attribute and value is the model object.
        """
        for child in root:
            model = Model(child)
            self.models[model.name] = model

    def _load_files(self, root):
        """
        Assumes the root is the <Files> XML tag. Adds file to one of two lists
        depending on type attribute.
        """
        #TODO, add real error checking to this
        for child in root:
            file_type = child.get('type', -1)
            file_path = child.get('path', -1)
            if file_type == 'test':
                self.test_files.append(file_path)
            elif file_type == 'train':
                self.train_files.append(file_path)
            else:
                print "Error: Type invalid for file"
