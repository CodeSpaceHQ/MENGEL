"""
Holds all test cases for configuration.py
"""
from unittest import TestCase
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.abspath('..'))
from configuration import Configuration
from configuration import ConfigurationError
from configuration import ConfigurationXMLError


def create_attributes(seed):
    """
    Only handles required info. Does NOT deal with <Files> or <Models>.
    Creates a dictionary of dictionaries where the initial key is the tag that
    is associated with the attributes described by the nested dictionary.
    """
    attributes = {}
    attributes['seed'] = seed

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
    if attributes.has_key('Firebase'):
        ET.SubElement(root, 'Firebase', attrib=attributes['Firebase'])

    if attributes.has_key('Prediction'):
        ET.SubElement(root, 'Prediction', attrib=attributes['Prediction'])

    return root

def create_attrib_files(attributes):
    """
    To be used after #create_xml_project.
    Creates dummmy test & train file names and adds to attributes under key:
    Files and the value is a dictionary with the key,value = path,type
    """
    files = {}
    for i in range(1, attributes['seed']%10):
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
    for i in range(1, attributes['seed']%5):
        model = {}
        model['name'] = 'model{}'.format(i)
        model['params'] = create_attrib_params(attributes['seed']%3 + (2*i))
        models[model['name']] = model

    attributes['Models'] = models
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
            for val in range(0, i+1):
                values.append('value{}'.format(val))
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
    for model in attributes['Models'].values():
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
        if key != 'values':
            param_attrib[key] = value
    element = ET.SubElement(root, 'Param', attrib=param_attrib)
    if attributes.has_key('values'):
        for value in attributes['values']:
            ET.SubElement(element, 'Value').text = value
    return root

class TestConfigurationBase(TestCase):
    """ Base class for all configuration tests to extend.

    Holds all common methods.
    """

    def setUp(self):
        """ Base setup for all test cases"""
        self.files_used = []

        # The following lines are to please linters
        self.config = None
        self.xml_root = None
        self.xml_file_name = None
        self.attributes = None

    def tearDown(self):
        """ Base teardown for all test cases"""
        self.xml_root = None
        for file_used in self.files_used:
            os.remove(file_used)

    def prep(self, filename):
        """ Handles all intializing. Attributes should be created before
        this method is run."""
        self.xml_file_name = filename
        self.create_xml_root()
        self.create_xml_file()

    def create_all_attributes(self, seed):
        """ Helper method for creating all atriibutes including file and models"""
        self.attributes = create_attributes(seed)
        self.attributes = create_attrib_files(self.attributes)
        self.attributes = create_attrib_models(self.attributes)

    def create_xml_root(self):
        """ Creates the XML object"""
        self.xml_root = create_xml_project(self.attributes)
        if self.attributes.has_key('Files'):
            self.xml_root = add_xml_files(self.attributes, self.xml_root)

        if self.attributes.has_key('Models'):
            self.xml_root = add_xml_models(self.attributes, self.xml_root)

    def create_xml_file(self):
        """ Writes the XML object created in #create_xml_root to file"""
        self.files_used.append(self.xml_file_name)

        tree = ET.ElementTree(self.xml_root)
        tree.write(self.xml_file_name)

    def check_config_data(self, tag):
        """
        Used to check the attributes of the second-level elements in the
        XML file.
        """
        expected = self.attributes[tag]
        actual = self.config.config_data[tag]
        self.compare_dicts(expected, actual)

    def check_model(self, exp_attrib, act_model):
        """
        More or less this just iterates through the models making sure the
        name field is correct before passing it's params to the check_param
        methods
        """
        self.assertEqual(exp_attrib['name'], act_model.name)
        self.assertEqual(len(exp_attrib['params']), len(act_model.params))
        for key, exp_param in exp_attrib['params'].items():
            self.assertTrue(act_model.params.has_key(key),\
                msg='Key = {}'.format(key))
            self.check_param(exp_param, act_model.params[key])

    def check_param(self, exp_attrib, act_param):
        """
        So there is one major difference when comparing parameters that are
        numeric vs ones that are not, and that difference is the 'values' field.
        Numeric ones do not have it. More importantly, we need to deal with the
        scenario where we do have a values field. The way the exp_attrib is
        setup, it will have an extra key (values) for holding the list of values.
        This extra key will mess up the comparision methods as the exp_attrib
        will have an extra key. So keep that in mind. Good luck.
        """

        self.assertTrue(act_param.details.has_key('numeric'))
        exp_attrib.pop('name', None)
        exp_len = len(exp_attrib) if exp_attrib['numeric'] == 'true' else len(exp_attrib)-1
        self.assertEqual(exp_len, len(act_param.details),\
            msg="act = {}\nexp={}".format(act_param.details, exp_attrib))

        if exp_attrib['numeric'] == 'false':
            self.compare_lists(exp_attrib['values'], act_param.values)
            exp_attrib.pop('values', None)

        self.compare_dicts(exp_attrib, act_param.details)

    def compare_dicts(self, dict1, dict2):
        """ Helper method for comparing two dictionaries."""
        self.assertEqual(len(dict1.keys()), len(dict2.keys()))
        for key, value in dict1.items():
            self.assertEqual(dict2[key], value,\
                msg='dict1[{}] = {} != dict2[{}]={}'.format(key, value, key, dict2[key]))

    def compare_lists(self, list1, list2):
        """ Helper method for comparing two lists, lists cannot can duplicate items"""
        self.assertEqual(len(list1), len(list2),\
            msg='list1={},\n list2={}'.format(list1, list2))
        interset = set(list1) & set(list2)
        self.assertEqual(len(interset), len(list1))

class TestConfigurationHappyPath(TestConfigurationBase):
    """ Happy Path Testing for XML file """
    def setUp(self):
        super(TestConfigurationHappyPath, self).setUp()
        self.create_all_attributes(5)
        self.prep('valid.xml')
        self.config = Configuration(self.xml_file_name)

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

    def test_configuration_models(self):
        """
        Tests that the models were correctly loaded into the
        configuration object.
        """
        exp_attrib = self.attributes['Models']
        act_models = self.config.models
        self.assertEqual(len(exp_attrib.keys()), len(act_models.keys()))
        for exp_key, exp_model in exp_attrib.items():
            self.assertTrue(act_models.has_key(exp_key))
            self.check_model(exp_model, act_models[exp_key])

    def test_configuration_save(self):
        """
        Tests the save method of the Confgiuration object.
        Essenetially what happens is this calls the save command on the
        Configuration object, uses it to create a new Congifuration object
        then compares the two.
        """
        output_name = "test_configuration_save.xml"
        self.files_used.append(output_name)
        self.assertEqual(self.config.project_name, self.attributes['project']['name'])
        self.config.save()
        self.config.save(output_name)
        config2 = Configuration(output_name)
        self.assertEqual(self.config.project_name, config2.project_name)
        self.assertEqual(self.config.user_name, config2.user_name)
        self.compare_lists(self.config.test_files, config2.test_files)
        self.compare_lists(self.config.train_files, config2.train_files)
        self.assertEqual(len(self.config.models.items()), len(config2.models.items()))
        for name, model in self.config.models.items():
            c2_model = config2.models[name]
            self.assertEqual(len(model.params.items()), len(c2_model.params.items()))
            for param_name, param in model.params.items():
                c2_param = c2_model.params[param_name]
                self.compare_lists(param.values, c2_param.values)
                self.compare_dicts(param.details, c2_param.details)

class TestConfigurationSadPath(TestConfigurationBase):
    """ Sad Path Testing for XML file """
    def test_configuration_bad_xml_root_tag(self):
        """ Tests having an inncorrect root tag in the XML file"""
        self.attributes = create_attributes(1) # It really doesnt matter cause the root tag is wrong
        self.xml_file_name = 'invalid_root_tag.xml'
        self.xml_root = ET.Element('MLF-Configuration', attrib=self.attributes['project'])
        self.create_xml_file()
        with self.assertRaises(ConfigurationXMLError):
            Configuration(self.xml_file_name)

    def test_configuration_bad_xml_project_attrib(self):
        """Tests missing the project attributes"""
        self.create_all_attributes(1)
        self.attributes['project'].pop('name', None)
        self.prep('test_configuration_bad_xml_project_attrib_name.xml')
        self.check_configuration_error()
        self.attributes['project']['name'] = 'TEST_PROJECT'
        self.attributes['project'].pop('user', None)
        self.prep('test_configuration_bad_xml_project_attrib_user.xml')
        self.check_configuration_error()

    def test_configuration_bad_xml_tags(self):
        """Tests missing required XMl tags such as Models and Files."""
        self.create_all_attributes(5)

        self.check_required_tag('Files')
        self.check_required_tag('Models')
        self.check_required_tag('Prediction')

    def test_configuration_bad_file_type(self):
        """ Tests having a file type that is not 'test' or 'train' """
        self.create_all_attributes(5)
        self.attributes['Files']['InvalidFile.cvs'] = 'nottest'
        self.prep('test_configuration_bad_file_type.xml')
        self.check_configuration_xml_error()


    def check_configuration_error(self):
        """ Helper method to check that the Configuration constructor
        raised a ConfigurationError. """
        with self.assertRaises(ConfigurationError):
            Configuration(self.xml_file_name)

    def check_configuration_xml_error(self):
        """ Helper method to check that the Configuration constructor
        raised a ConfigurationXMLError. """
        with self.assertRaises(ConfigurationXMLError):
            Configuration(self.xml_file_name)

    def check_required_tag(self, tag):
        """ Helper method to help reduce code in #test_configuration_bad_xml_tags
        """
        temp_data = self.attributes[tag]
        self.attributes.pop(tag, None)
        self.prep('test_configuration_bad_xml_tags_{}.xml'.format(tag))
        self.check_configuration_xml_error()
        self.attributes[tag] = temp_data
        self.check_configuration_xml_error()
