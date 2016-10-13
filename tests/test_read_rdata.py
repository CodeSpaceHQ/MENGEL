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
        data_set  = pd.read_csv("/Users/ryanberg/Desktop/Real SE2/SE2-KaggleComp/datasets/testfile.csv", index_col = False)
        data_set = pd.DataFrame(data_set)
        # Act
        f = read.reader()
        data_test = f.Read_rds("/Users/ryanberg/Desktop/Real SE2/SE2-KaggleComp/datasets/testfile.rds")

        # Assert
        self.assertEqual(type(data_test), type(data_set))