#!/usr/bin/python
""" MLTA Record Python API Docstring
This module serves as a Python API for the mlta-record command line.

Example:
    from mlta import record # One of several ways you can import this file

    # Create project and record
    example_project = record.Project("Example_Project")
    example_record = record.ResultRecord("Example_Model_Type")

    # Add model data to the record
    example_record.add_model_data_pair("model_key1","model_val1")
    example_record.add_model_data_pair("model_key3","model_val2")
    example_record.add_model_data_pair("model_key2","model_val3")

    # Add test data to the record
    example_record.add_test_data_pair("test_key","test_val")

    # Add record to the project
    example_project.add_record(example_record)

    # Save all records added to the project
    example_project.save_all_records()

"""

import subprocess

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class MLTAError(Error):
    """ Generic MLTA Error, this should be the only error thrown out of this file """
    def __init__(self, message):
        Error.__init__(self)
        self.message = message

class MLTARecordError(Error):
    """ Used internally to catch errors specifically from dealing with the mlta-record command. """
    def __init__(self, message, args):
        Error.__init__(self)
        self.message = message
        self.args = args

class Project(object):
    """ This is the class that matches what is stored in the database. """

    def __init__(self, name):
        self.name = name
        self.records = []

    def add_record(self, record):
        """ Add a record to the list of records for this project. """
        record.projectName = self.name
        self.records.append(record)

    def save_all_records(self):
        """ Goes through the list of records for this project and saves each
        one of them in the database. """
        for record in self.records:
            self.save_record(record)

    def save_record(self, record):
        """ Calls 'mlta-record' to save this record to the Firebase databse. """
        args = self._get_args(record)
        try:
            program_result = self._call_mlta_record(args)
            return program_result
        except MLTARecordError as exception:
            raise MLTAError('Unable to save record. Reason: {} '.format(exception.message))

    def _get_data_args(self, data,opt):
        """If model then opt = -d else -D"""
        args = []
        for key, val in data.items():
            args.append(opt)
            args.append("{}:{}".format(key, val))

        return args

    def _get_args(self, record):
        """ Internal method used to create the args string needed to run the
        'mlta-record' command """
        args = ["mlta-record", "-p", self.name, "-m", \
            "{}".format(record.model_type)]

        args.extend(self._get_data_args(record.model_data, '-d'))
        args.extend(self._get_data_args(record.test_data, '-D'))

        return args

    # More or less just a wrapper around the system call
    # Returns key
    def _call_mlta_record(self, args):
        """ Internal method used to call 'mlta-record'.
        This was broken out into it's own method to make testing easier."""
        try:
            result = subprocess.check_output(args).splitlines()
            if result[0] != '0':
                try:
                    raise MLTARecordError("MLTA-Record returned an error: {}".format(result[1]), args)
                except IndexError:
                    raise MLTARecordError("MLTA-Record return an error with args: {}".format(args), args)
            else:
                return result[1]
        except OSError as exception:
            raise MLTARecordError('There was an OS error', exception)



# Data Members
# - model_type
# - model_data
# - label
# - test_data
class ResultRecord(object):
    """ This class holds all the data to be stored in the database for an
    indivdual test on an algorithm. This object cannot be directly saved to the
    database but should be added to a Project object which will handle saving.
    """

    def __init__(self, model_type):
        self.model_type = str(model_type)
        self.model_data = {}
        self.test_data = {}
        self.label = ""

    def _add_data_pair(self, data, key, value):
        """ Generic code to be used by 'add_model_data_pair' and
        'add_test_data_pair' for adding a data pair to the record."""
        key = str(key)
        value = str(value)
        if data.has_key(key):
            print "Error: key {} already exists".format(key)
        else:
            data[key] = value

    def add_model_data_pair(self, key, value):
        """ Adds the given in key, value pair to the the model_data list """
        self._add_data_pair(self.model_data, key, value)

    def add_test_data_pair(self, key, value):
        """ Adds the given in key, value pair to the the test_data list """
        self._add_data_pair(self.test_data, key, value)

    def print_data(self):
        """ Helper method to print the data to STDOUT """
        print "Model Data"
        for key, val in self.model_data.items():
            print key, '>', val

        print ''
        print "Test Data"
        for key, val in self.test_data.items():
            print key, '>', val
