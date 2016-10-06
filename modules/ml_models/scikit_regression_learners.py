from sklearn import linear_model
from sklearn import svm


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
def train_bayesian_ridge(validation_pack, data_pack):
    # Picking model
    return linear_model.BayesianRidge()


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
def train_support_vector_regression(validation_pack, data_pack):
    # Picking model
    return svm.SVR()
