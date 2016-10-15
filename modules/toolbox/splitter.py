"""
Ryan Berg - updated 9/24/16

User Story: As a user I want to split a dataset into training and testing files.

"""


import sys
import subprocess
import os

scriptpath = os.path.dirname(os.path.realpath(__file__)) + "/r_split.R"

class Splitter:

    def __init__(self):
        return

    """
    input: filepath to desired .csv file to split (must be .csv), as well as separater type
    ("," or "\;" - note the escape character is necessary for ";" delimited files)
    output: two datasets, one for training one for testing. (output will be in.csv form and .rda)

    """

    def Split(self, filepath, separator):
        args = [filepath]
        sep = [separator]
        cmd = ["Rscript", scriptpath] + args + sep
        subprocess.call(cmd)


if __name__ == "__main__":
    filepath = sys.argv[1]
    separator = sys.argv[2]
    split = Splitter()
    split.Split(filepath, separator)
