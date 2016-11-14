from sklearn import linear_model
from sklearn import svm
from modules.DMZ.models import model_properties as mp


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
def train_bayesian_ridge():
    # Picking model
    return mp.ModelProperties(regression=True), linear_model.BayesianRidge()


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
def train_support_vector_regression():
    # Picking model
    return mp.ModelProperties(regression=True), svm.SVR()
