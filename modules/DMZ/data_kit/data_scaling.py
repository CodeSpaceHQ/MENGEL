from sklearn import preprocessing
import numpy as np


# Scales the numeric input data.
# Input:
# - Pandas Dataframe, non-scaled
# Output:
# - Pandas Dataframe that has been scaled.
def scale_numeric_data(pandas_data):
    # Scaling is important because if the variables are too different from
    # one another, it can throw off the model.
    # EX: If one variable has an average of 1000, and another has an average
    # of .5, then the model won't be as accurate.
    for col in pandas_data.columns:
        if pandas_data[col].dtype == np.float64 or pandas_data[col].dtype == np.int64:
            pandas_data[col] = preprocessing.scale(pandas_data[col])

    return pandas_data


# Creates a standard scaler based on the training data and applies it to both train
# and test data.
# Input:
# - Two Pandas DataFrames, same number of columns
# Output:
# - Two Pandas DataFrames, both of which have been scaled based on StandardScaler
# trained on training data.
def scale_data(train, test):
    scaler = preprocessing.StandardScaler().fit(train)

    return scaler.transform(train), scaler.transform(test)
