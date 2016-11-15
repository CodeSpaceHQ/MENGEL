"""
Ryan Berg 10/19/16
"""

import sys
import pandas as pd
import numpy as np
from rpy2.robjects import DataFrame
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import  importr
pandas2ri.activate()

# Imports for the R libraries needed
rparty = importr("rpart")
base = importr("base")
stats = importr("stats")

class Rpart:


    def __init__(self):
        self.model = pd.DataFrame
        self.error_matrix = pd.DataFrame
        self.outcome = ""
        self.accuracy = 0


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

        #train the model
        model = rparty.rpart(formula = formula,
                             data = train_data,
                             method = "class"
                             #control = rparty.rpart_control(minsplit = ?, cp = ?)
                             )

        self.model = model
        return model


    #Uses a model to make predictions on a dataset.
    def predict(self, model, dataset):
        """
        :param model: an rpart model created during fit function
        :param dataset: dataset in which we are using the model to predict
        :return: an error matrix based on the model and dataset input into the function
        """

        pred = stats.predict(model, type = "class")
        self.error_matrix = base.table(pred, dataset[self.outcome])
        return self.error_matrix


    def score(self):
        """
        :return: accuracy of model with respect to test data input into predict function
        """


        numerator = pd.DataFrame.sum(pd.DataFrame(np.diag(self.error_matrix)))[0]
        denominator = pd.DataFrame.sum(pd.DataFrame(np.ndarray.flatten(np.asarray(self.error_matrix))))[0]

        self.accuracy = float(numerator)/float(denominator)
        return self.accuracy



if __name__ == "__main__":

    train_data = sys.argv[1]
    predictor = sys.argv[2]
    train_data = pd.read_csv(train_data, delimiter= ";")
    train_data = pd.DataFrame(train_data)
    rpart = Rpart()
    rpart.fit(train_data, predictor)
    rpart.predict(rpart.model, train_data)



