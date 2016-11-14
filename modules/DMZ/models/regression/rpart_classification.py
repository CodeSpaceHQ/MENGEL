"""
Ryan Berg 10/19/16
"""

import sys
import subprocess
import os
import pandas as pd
from rpy2.robjects import DataFrame, Formula, pandas2ri, importr
pandas2ri.activate()
rparty = importr('rpart')
proc = importr("pRoc")

scriptpath = os.path.dirname(os.path.realpath(__file__)) + "/r_classification.R"
scorescript = os.path.dirname(os.path.realpath(__file__)) + "/r_rpartpredict.R"

class Rpart:

    def __init__(self):
        self.model = pd.DataFrame
        self.score = pd.DataFrame

    #Needed to send R data it can work with rather than a pandas dataframe.
    

    #Returns a probability matrix, based on data results.
    def score(self, trained_results, actual_data):
        return self.score

    #Trains the model.
    def fit(self, test_data,  target):
        test_d = [self.convert_to_rdata(test_data)]
        target = [target]
        cmd = ["Rscript", scriptpath] + test_d + target
        subprocess.call(cmd)

    #Uses a model to make predictions on a dataset.
    def predict(self, model, dataset):
        command = ["Rscript", scorescript] + [model] + [dataset]
        self.score = subprocess.call(command)


if __name__ == "__main__":
    test_data = sys.argv[1]
    #train_data = sys.argv[2]
    predictor = sys.argv[2]
    rpart = Rpart()
    train_data_fun = DataFrame(pd.read_csv(test_data))
    formula = Formula(predictor + " ~ .")
    model = rparty.rpart(formula = formula, data = train_data_fun)
    print(model)
    #rpart.fit(train_data_fun, predictor)