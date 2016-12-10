from sklearn import linear_model
from sklearn import svm
import xgboost
from modules.DMZ.models import model_properties as mp


# All functions return a tuple with the properties of the model and the object that represents the model.


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
def train_bayesian_ridge():
    # Picking model
    return mp.ModelProperties(regression=True), linear_model.BayesianRidge()


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
def train_support_vector_regression():
    # Picking model
    return mp.ModelProperties(regression=True), svm.SVR()


# http://xgboost.readthedocs.io/en/latest/python/python_api.html
def train_xgboost_regressor():
    return mp.ModelProperties(regression=True), xgboost.XGBRegressor()
