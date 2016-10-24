"""
Ryan Berg 10/19/16



"""


import sys
import subprocess
import os

scriptpath = os.path.dirname(os.path.realpath(__file__)) + "/r_classification.R"

class Rpart:

    def __init__(self):
        return

    def rpart_classify(self, test_data_filepath, train_data_filepath, predictor):
        test_d = [test_data_filepath]
        train_d = [train_data_filepath]
        pred = [predictor]
        cmd = ["Rscript", scriptpath] + test_d + train_d + pred
        subprocess.call(cmd)

if __name__ == "__main__":
    test_data = sys.argv[1]
    train_data = sys.argv[2]
    predictor = sys.argv[3]
    rpart = Rpart()
    rpart.Rpart(test_data, test_data)