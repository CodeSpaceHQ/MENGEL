import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.ml_models import scikit_online_learners
import setup

class TestOnlineLearning(TestCase):
    def test_sgd_regressor(self):
        result = scikit_online_learners.run_sgd_regressor(setup.get_datasets_path(), "winequality-red.csv", ';')
        self.assertGreater(result, 0, msg="Failed to beat baseline")
    
    def test_passive_aggressive_regressor(self):
        result = scikit_online_learners.run_passive_aggressive_regressor(setup.get_datasets_path(), "winequality-red.csv", ';')
        self.assertGreater(result, 0, msg="Failed to beat baseline")
