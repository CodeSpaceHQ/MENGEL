"""
Ryan Berg - updated 9/30/16

User Story: As a user I want to merge multiple dataset files.


"""

import sys
import subprocess
import os

scriptpath = os.getcwd()+ "/r_merge.R"

class Merger:
    """
    input: A column name (String) for the datasets to be merged on, as well as the filepaths for all of the files to be merged.

    output: one dataset, that is all of the datasets full_joined, in both .csv and .rda format.
    """

    def merge(files):
        args = files
        cmd = ["Rscript", scriptpath] + args
        subprocess.call(cmd)


    if __name__ == "__main__":

        files = []

        for i in range(1,len(sys.argv)):
            files = files + [sys.argv[i]]

        merge(files)
