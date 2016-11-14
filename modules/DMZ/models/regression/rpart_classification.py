"""
Ryan Berg 10/19/16
"""

import sys
import pandas as pd
from rpy2.robjects import DataFrame, Formula, pandas2ri
from rpy2.robjects.packages import  importr
pandas2ri.activate()

# Imports for the R libraries needed
rparty = importr('rpart')
proc = importr("pROC")
base = importr("base")
stats = importr("stats")
caret = importr("caret")

class Rpart:

    def __init__(self):
        self.model = pd.DataFrame
        self.score = pd.DataFrame
        self.outcome = ""

    #Returns a probability matrix, based on data results.
    def score(self):
        return self.score

    #Trains the model.
    def fit(self, training_data,  target):
        """
        :param training_data: a pandas dataframe.
        :param target: a string referring to the target varialbe to be predicted
        :return: An rpart model
        """

        self.outcome = target
        #Converting to proper format for R functions
        train_data = DataFrame(training_data)
        formula = target + " ~ ."

        #TODO: HyperParameter Incorporateion

        model = rparty.rpart(formula = formula,
                             data = train_data,
                             method = "class"
                             #control = rparty.rpart_control(minsplit = ?, cp = ?)
                             )

        self.model = model
        return model

    #Uses a model to make predictions on a dataset.
    def predict(self, model, dataset):
        pred = stats.predict(model, dataset, type = "class")
        print(base.table(pred, dataset[self.outcome]))
        return

if __name__ == "__main__":
    train_data = sys.argv[1]
    predictor = sys.argv[2]

    train_data = pd.read_csv(train_data, delimiter= ";")
    train_data = pd.DataFrame(train_data)

    rpart = Rpart()
    rpart.fit(train_data, predictor)
    rpart.predict(rpart.model, train_data)
    print(rpart.model)
