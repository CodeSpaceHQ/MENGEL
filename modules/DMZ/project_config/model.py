#!/usr/bin/python
""" Model
Holds all data and methods to manipluate said data for a single model.

"""

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ModelError(Exception):
    """Generic error for Model & Param.

     Used for exceptions created in this module that do not have a specific
     exception for them."""

    def __init__(self, message):
        super(ModelError, self).__init__(message)
        self.message = message

class ModelXMLError(Exception):
    """ XML File error for Model & Param.

    Error for exceptions created by Configuration that specifically have to
    deal with the XML file. """

    def __init__(self, message, trouble_xml):
        super(ModelXMLError, self).__init__(message)
        self.message = message
        self.bad_xml = trouble_xml

class Param(object):
    """Holds attributes and values for a given hyper parameter"""
    def __init__(self, root):
        super(Param, self).__init__()
        self.details = {}
        self.values = []
        if not root.attrib.has_key('name'):
            raise ModelXMLError('Required Param XML attribute [name] not found',\
            root)
        for key, value in root.items():
            if key == 'name':
                self.name = value
            else:
                self.details[key] = value

        for child in root:
            self.values.append(child.text)

class Model(object):
    """Holds attribute data and a list of Param objects for a given model"""
    def __init__(self, root):
        super(Model, self).__init__()
        attributes = root.attrib
        if(attributes.has_key('name')):
            self.name = attributes['name']
        else:
            raise ModelXMLError('Required Model XML attribute [name] not found'\
            , root)

        self.params = {}
        for child in root:
            param = Param(child)
            self.params[param.name] = param
