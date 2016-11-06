#!/usr/bin/python
""" Model
Holds all data and methods to manipluate said data for a single model.

"""
class Param(object):
    """Holds attributes and values for a given hyper parameter"""
    def __init__(self, root):
        super(Param, self).__init__()
        self.details = {}
        self.values = []
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
        self.name = root.attrib.get('name')
        self.params = {}
        for child in root:
            param = Param(child)
            self.params[param.name] = param
