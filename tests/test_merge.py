import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import merge as mg
import setup


class TestMerge(TestCase):

    def test_merge(self):

        full_csv = False
        full_rds = False
        # Arrange
        filepath = setup.get_datasets_path() + "titanic_train.csv"


        # Act
        merge = mg.Merger()
        merge.merge(["Name", filepath, filepath, filepath])

        for File in os.listdir(setup.get_datasets_path()):
            if File.endswith("full.dataset.csv"):
                full_csv = True
            if File.endswith("full.dataset.rds"):
                full_rds = True
        # Assert
        self.assertEqual(full_csv, True)
        self.assertEqual(full_rds, True)
