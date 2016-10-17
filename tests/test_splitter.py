import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import splitter as sp
import setup

class TestSplitter(TestCase):

    def test_Split_one(self):
        # Arrange
        filepath = setup.get_datasets_path()
        splitter = sp.Splitter();
        splitter.Split((filepath + "testfile.csv"), ",")

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

    def test_split_two(self):

        #Arrange
        filepath = setup.get_datasets_path()
        splitter = sp.Splitter();
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
