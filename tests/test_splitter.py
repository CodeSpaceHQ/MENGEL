import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from unittest import TestCase
from modules.toolbox import splitter as sp
import setup

class TestSplitter(TestCase):

    def test_Split(self):
        sp.Splitter.Split("filepath")

        self.assertEquals = (train, train)
        self.assertEquals = (test, test)