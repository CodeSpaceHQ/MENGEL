import csv
import pandas as pd


# A standard way of retrieving data, separating this out in case we need to change it.
def get_data(path, filename):
    return pd.read_csv(path + filename, sep=None)


# A standard way to save the results of an applied model on an unlabeled test data set
def save_predictions(path, predictions, filename):
    with open(path + filename + "_predictions.csv", 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(predictions)
