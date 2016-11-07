#!/usr/bin/python
from unittest import TestCase
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.abspath('..'))
from configuration import Configuration


def create_addtributes():
    """
    Only handles required info. Does NOT deal with <Files> or <Models>.
    Creates a dictionary of dictionaries where the initial key is the tag that
    is associated with the attributes described by the nested dictionary.
    """
    attributes = {}

    project_attributes = {}
    project_attributes['name'] = 'PROJECT_NAME'
    project_attributes['user'] = 'USER_NAME'
    attributes['project'] = project_attributes

    firebase_attributes = {}
    firebase_attributes['url'] = 'FirebaseDatabaseURL'
    firebase_attributes['account'] = 'FullPathToServiceAccount'
    attributes['Firebase'] = firebase_attributes

    prediction_attributes = {}
    prediction_attributes['target'] = 'TARGET'
    prediction_attributes['type'] = 'TYPE'
    attributes['Prediction'] = prediction_attributes

    return attributes

def create_xml_project(attributes):
    """
    Only handles required info. Does NOT deal with <Files> or <Models>.
    Creates an ET.Element object that acts as the root of the XML file. Uses
    passed in attributes object to define attributes of XML.
    """
    root = ET.Element('MLTF-Configuration', attrib=attributes['project'])
    ET.SubElement(root, 'Firebase', attrib=attributes['Firebase'])
    ET.SubElement(root, 'Prediction', attrib=attributes['Prediction'])

    return root

class TestConfigurationValidXML(TestCase):
    """ Happy Path Testing for XML file """
    def setUp(self):
        # Create attributes
        self.attributes = create_addtributes()
        self.xml_root = create_xml_project(self.attributes)
        self.xml_file_name = 'valid.xml'

        tree = ET.ElementTree(self.xml_root)
        tree.write(self.xml_file_name)
        self.config = Configuration(self.xml_file_name)

    def tearDown(self):
        self.xml_root = None
        os.remove(self.xml_file_name)

    def test_configuration_properties(self):
        """ Tests that basic data (properties) are correct"""
        self.assertEqual(self.config.config_file_name, self.xml_file_name)
        self.assertEqual(self.config.project_name, self.attributes['project']['name'])
        self.assertEqual(self.config.user_name, self.attributes['project']['user'])

    def test_configuration_firebase(self):
        """ Tests that the firebase information is correct."""
        self.check_config_data('Firebase')

    def test_configuration_prediction(self):
        """ Tests that the prediction information is correct. """
        self.check_config_data('Prediction')


    def check_config_data(self,tag):
        expected = self.attributes[tag]
        actual = self.config.config_data[tag]
        for key, value in expected.items():
            self.assertEqual(actual[key],value)
