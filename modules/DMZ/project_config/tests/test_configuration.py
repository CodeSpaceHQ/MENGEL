"""
Holds all test cases for configuration.py
"""
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

def create_attrib_files(attributes):
    """
    To be used after #create_xml_project.
    Creates dummmy test & train file names and adds to attributes under key:
    Files and the value is a dictionary with the key,value = path,type
    """
    files = {}
    for i in range(1, 5):
        files['/path/to/test/file{}'.format(i)] = 'test'
        files['/path/to/train/file{}'.format(i)] = 'train'

    attributes['Files'] = files

    return attributes

def create_attrib_models(attributes):
    """
    To be used after #create_xml_project.
    Creates dummmy test & train file names and adds to attributes under key:
    Models and the value is a dictionary of dictionaries with
    key,value = model name, a dictionary of params where the nest dictionary is
    key,value = param attribute, param value
    Each param is guarenteed to have a name & numeric attribute.
    If number=false, then there will be a value attribute with a list of values.
    """
    models = {}
    for i in range(1, 2):
        model = {}
        model['name'] = 'model{}'.format(i)
        model['params'] = create_attrib_params(3)#i+(2*i))
        models[model['name']] = model

    attributes['models'] = models
    return attributes


def create_attrib_params(seed):
    """ returns a dictionary of random generated params """
    params = {}

    for i in range(1, seed):
        param = {}
        param['name'] = 'Param{}'.format(i)
        if i%2 == 0: # If i is even, create a numeric param
            param['numeric'] = 'true'
            param['defaultValue'] = str(i+1)
            param['delta'] = str(seed/4)
            param['rangeStart'] = str(i)
            param['rangeEnd'] = str(seed)
        else: # Create a non-numeric param
            param['numeric'] = 'false'
            param['defaultValue'] = 'somevalue'
            values = []
            for v in range(0, i+1):
                values.append('value{}'.format(v))
            param['values'] = values
        params[param['name']] = param
    return params


def add_xml_files(attributes, root):
    """
    To be used after #create_attrib_files
    Adds the dummy data generated to the passed in root.
    """
    file_element = ET.SubElement(root, 'Files')
    for key, value in attributes['Files'].items():
        file_attrib = {}
        file_attrib['type'] = value
        file_attrib['path'] = key
        ET.SubElement(file_element, 'File', attrib=file_attrib)

    return root

def add_xml_models(attributes, root):
    """"
    To be used after #create_attrib_models
    Adds the dummy data generated to the passed in root.
    """
    models_element = ET.SubElement(root, 'Models')
    for model in attributes['models'].values():
        model_attrib = {}
        model_attrib['name'] = model['name']
        model_element = ET.SubElement(models_element, 'Model', attrib=model_attrib)
        for param in model['params'].values():
            add_xml_param(param, model_element)

    return root


def add_xml_param(attributes, root):
    """
    To be used in #add_xml_models
    Assumes root is the <Model> tag
    Assumes attributes is all the params
    """
    param_attrib = {}

    for key, value in attributes.items():
        #print(key, ' ', value)
        if key != 'values':
            param_attrib[key] = value
    print(param_attrib)
    element = ET.SubElement(root, 'Param', attrib=param_attrib)
    if attributes.has_key('values'):
        for value in attributes['values']:
            ET.SubElement(element,'Value').text=value
    return root


class TestConfigurationValidXML(TestCase):
    """ Happy Path Testing for XML file """
    def setUp(self):
        # Create attributes
        self.attributes = create_addtributes()
        self.attributes = create_attrib_files(self.attributes)
        self.attributes = create_attrib_models(self.attributes)
        self.xml_root = create_xml_project(self.attributes)

        self.xml_root = add_xml_files(self.attributes, self.xml_root)
        self.xml_root = add_xml_models(self.attributes, self.xml_root)

        self.xml_file_name = 'valid.xml'

        tree = ET.ElementTree(self.xml_root)
        ET.dump(tree)
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

    def test_configuration_files(self):
        """ Tests that the files were all loaded and added to the correct list."""
        exp = self.attributes['Files']
        act_test = self.config.test_files
        act_train = self.config.train_files
        self.assertEqual(len(act_test) + len(act_train), len(exp.keys()))

        for test_file in act_test:
            self.assertEqual(exp[test_file], 'test')

        for train_file in act_train:
            self.assertEqual(exp[train_file], 'train')




    def check_config_data(self, tag):
        expected = self.attributes[tag]
        actual = self.config.config_data[tag]
        for key, value in expected.items():
            self.assertEqual(actual[key], value)

    def compare_lists(self, list1, list2):
        self.assertEqual(len(list1), len(list2))
        interset = set(list1) & set(list2)
        self.assertEqual(len(interset), len(list1))
