import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import merge as mg
import setup


class TestMerge(TestCase):
