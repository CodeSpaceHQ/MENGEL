#!/usr/bin/python
from unittest import TestCase
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from configuration import Configuration


class TestConfigurationValidXML(TestCase):
    def setUp(self):
        self.config = Configuration('sample.xml')


    def test_configuration_properties(self):
        """ Tests that basic data (properties) are correct"""
        self.assertEqual(self.config.config_file_name,'sample.xml')
        self.assertEqual(self.config.project_name,'SE2-KaggleComp')
        self.assertEqual(self.config.user_name,'asclines')
