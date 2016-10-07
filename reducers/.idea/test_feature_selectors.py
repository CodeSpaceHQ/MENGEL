import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from reducers import scikit_feature_selectors
import setup

class TestFeatureSelectors(TestCast):

    def test_VarianceThreshold_selector(self):
