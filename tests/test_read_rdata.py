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
        x = setup.get_datasets_path()
        data_set  = pd.read_csv(x + "testfile.csv", index_col = False)
        data_set = pd.DataFrame(data_set)

        # Act
        f = read.reader()
        data_test = f.Read_rds(x + "testfile.rds")

        # Assert
        self.assertEqual(type(data_test), type(data_set))
