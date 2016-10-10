"""
Ryan Berg - updated 9/24/16

User Story: As a user I want to split a dataset into training and testing files.

"""


import sys
import subprocess
import os

scriptpath = os.getcwd() + "/modules/toolbox/r_split.R"

class Splitter:

    def __init__(self):
        return

    """
    input: filepath to desired .csv file to split (must be .csv)
    output: two datasets, one for training one for testing. (output will be in.csv form and .rda
    """

    def Split(self, filepath):
        args = [filepath]
        cmd = ["Rscript", scriptpath] + args
        subprocess.call(cmd)


    if __name__ == "__main__":
        filepath = sys.argv[1]
        Split(filepath)
