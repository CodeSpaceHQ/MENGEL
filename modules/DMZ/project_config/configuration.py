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
    """Generic error for Configuration.

     Used for exceptions created in this module that do not have a specific
     exception for them."""

    def __init__(self, message):
        super(ConfigurationError, self).__init__(message)
        self.message = message

class ConfigurationXMLError(Exception):
    """ XML File error for Configuration.

    Error for exceptions created by Configuration that specifically have to
    deal with the XML file. """

    def __init__(self, message, trouble_xml):
        super(ConfigurationXMLError, self).__init__(message)
        self.message = message
        self.bad_xml = trouble_xml

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

    def save(self, filename='-1'):
        """ Saves the configuration to an XML file output"""
        if filename == '-1':
            filename = self.config_file_name

        #Update models
        for model_xml in self.root.iter('Model'):
            model = self.models[model_xml.get('name')]
            for param_xml in model_xml.iter('Param'):
                param = model.params[param_xml.get('name')]
                for detail, value in param.details.items():
                    param_xml.set(detail, value)
        self.tree.write(filename)

    def _load_file(self):
        """ Loads the XML file and checks root tag for validaty"""
        self.tree = ET.parse(self.config_file_name)
        self.root = self.tree.getroot()
        required_tags = {}
        required_tags[TAG_MODELS] = 0
        required_tags[TAG_FILES] = 0
        required_tags['Prediction'] = 0

        if not self.root.tag == TAG_ROOT:
            raise ConfigurationXMLError('Required XML root tag [{}] not found \
in {}'.format(TAG_ROOT, self.config_file_name), self.root)

        if self.root.attrib.has_key('name'):
            self.project_name = self.root.attrib.get('name')
        else:
            raise ConfigurationError('Project name not defined.')

        if self.root.attrib.has_key('user'):
            self.user_name = self.root.attrib.get('user', '')
        else:
            raise ConfigurationError('User name not defined.')

        for child in self.root:
            if required_tags.has_key(child.tag):
                required_tags[child.tag] = 1
            if child.tag == TAG_MODELS:
                self._load_models(child)
            elif child.tag == TAG_FILES:
                self._load_files(child)
            else:
                self.config_data[child.tag] = child.attrib

        for key, value in required_tags.items():
            if value == 0:
                raise ConfigurationXMLError('Required XML tag [{}] not found \
                in {}'.format(key, self.config_file_name), self.root)



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
        for child in root:
            file_type = child.get('type', -1)
            file_path = child.get('path', -1)
            if file_type == 'test':
                self.test_files.append(file_path)
            elif file_type == 'train':
                self.train_files.append(file_path)
            else:
                raise ConfigurationXMLError('Invalid file type value: {}'.format(file_type), child)
