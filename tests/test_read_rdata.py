import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import read_rdata as read
import setup


class TestMerge(TestCase):

    def test_merge(self):

        # Arrange
        data_set  = pd.read_csv("testfile.csv")
        data_set = pd.DataFrame.from_csv(data_set)

        # Act
        data_test = read.reader.Read_rds("testfile.rds")

        # Assert
        self.assertEqual(data_set, data_test, msg="Test Successful")