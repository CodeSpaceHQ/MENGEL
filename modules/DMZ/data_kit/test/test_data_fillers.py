import os
import sys

sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_filler
from modules.DMZ.utils import test_prep


class TestDataFilling(TestCase):

    def test_drop_missing_data_rows(self):

        start, end = test_prep.prep_data_filler_tests_droppers("drop_rows")

        self.assertLess(end[0], start[0], msg="Failed to remove any rows")

    def test_drop_missing_data_columns(self):

        start, end = test_prep.prep_data_filler_tests_droppers("drop_cols")

        self.assertLess(end[1], start[1], msg="Failed to remove any columns")

    def test_drop_all_missing_data_columns(self):

        start, end = test_prep.prep_data_filler_tests_droppers("drop_all_cols")

        self.assertLess(end[1], start[1], msg="Failed to remove any columns")

    def test_drop_all_missing_data_rows(self):

        start, end = test_prep.prep_data_filler_tests_droppers("drop_all_rows")

        self.assertLess(end[0], start[0], msg="Failed to remove any rows")

    def test_fill_missing_data(self):

        data = test_prep.prep_data_filler_tests_fillers("fill_values")

        self.assertFalse(data.isnull().values.any(), msg="Failed to replace all NaNs")

    def test_fill_missing_data_average(self):

        data = test_prep.prep_data_filler_tests_fillers("fill_averages")

        self.assertFalse(data.isnull().values.any(), msg="Failed to replace all NaNs")
