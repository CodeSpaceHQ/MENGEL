import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import splitter as sp
import setup

class TestSplitter(TestCase):


    # test_comma_split tests the functionality of the splitter, with the delimiter as a comma.


    def test_comma_split(self):

        # Arrange
        filepath = setup.get_datasets_path()
        splitter = sp.Splitter()
        splitter.Split((filepath + "titanic_train.csv"), ",")

        #Act
        test_csv = False
        train_csv = False
        test_rds = False
        train_rds = False
        for File in os.listdir(filepath):
            if File.endswith(".testing.data.csv"):
                test_csv = True
            if File.endswith(".training.data.csv"):
                train_csv = True
            if File.endswith(".training.data.rds"):
                train_rds = True
            if File.endswith(".testing.data.rds"):
                test_rds = True

        # Assert
        self.assertEquals = (test_csv, True)
        self.assertEquals = (train_csv, True)
        self.assertEquals = (test_rds, True)
        self.assertEquals = (train_rds, True)


    # test_semicolon_split tests the functionality of the splitter, with the delimiter as a semicolon.

    def test_semicolon_split(self):

        #Arrange

        filepath = setup.get_datasets_path()
        splitter = sp.Splitter()
        splitter.Split((filepath + "winequality-red.csv"), ";")

        #Act
        test_csv = False
        train_csv = False
        test_rds = False
        train_rds = False
        for File in os.listdir(filepath):
            if File.endswith(".testing.data.csv"):
                test_csv = True
            if File.endswith(".training.data.csv"):
                train_csv = True
            if File.endswith(".training.data.rds"):
                train_rds = True
            if File.endswith(".testing.data.rds"):
                test_rds = True

        # Assert
        self.assertEquals = (test_csv, True)
        self.assertEquals = (train_csv, True)
        self.assertEquals = (test_rds, True)
        self.assertEquals = (train_rds, True)
