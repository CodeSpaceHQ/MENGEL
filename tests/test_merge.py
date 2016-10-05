import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import merge as mg
import setup


class TestMerge(TestCase):

    def test_merge(self):

        # Arrange
        data_set  = pd.read_csv("testfile")

        # Act
        mg.Merger.merge(["Variable", "filepath1", "filepah2", "filePath3"])
        data_test = pd.read_csv("full.dataset.csv")

        # Assert
        self.assertEqual(data_set, data_test, msg="Test Successful")