import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import splitter as sp
import setup

class TestSplitter(TestCase):

    # test_comma_split tests the functionality of the splitter, with the delimiter as a comma.
    test_csv = False
    train_csv = False
    test_rds = False
    train_rds = False
    filepath = setup.get_datasets_path()

    def helper(self):
        self.test_csv = False
        self.train_csv = False
        self.test_rds = False
        self.train_rds = False
        for File in os.listdir(self.filepath):
            if File.endswith(".testing.data.csv"):
                self.test_csv = True
                os.remove(self.filepath + File)
            if File.endswith(".training.data.csv"):
                self.train_csv = True
                os.remove(self.filepath + File)
            if File.endswith(".training.data.rds"):
                self.train_rds = True
                os.remove(self.filepath + File)
            if File.endswith(".testing.data.rds"):
                self.test_rds = True
                os.remove(self.filepath + File)

    def split_body(self, path, delim):

        #Arrange
        splitter = sp.Splitter()
        splitter.Split(path, delim)

        #Act
        self.helper()

        #Assert
        self.assertEquals = (self.test_csv, True)
        self.assertEquals = (self.train_csv, True)
        self.assertEquals = (self.test_rds, True)
        self.assertEquals = (self.train_rds, True)

    def test_comma_split(self):
        self.split_body(self.filepath + "titanic_train.csv", ",")

    # test_semicolon_split tests the functionality of the splitter, with the delimiter as a semicolon.
    def test_semicolon_split(self):
        self.split_body(self.filepath + "winequality-red.csv", ";")
