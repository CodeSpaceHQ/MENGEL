from sklearn import linear_model
from modules.DMZ.models import model_properties as mp


# All functions return a tuple with the properties of the model and the object that represents the model.


# "Linear model fitted by minimizing a regularized empirical loss with SGD"
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor
def train_sgd_regressor():
    # Picking model
    return mp.ModelProperties(regression=True, online=True), linear_model.SGDRegressor()


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
def train_passive_aggressive_regressor():
    # Picking model
    return mp.ModelProperties(regression=True, online=True), linear_model.PassiveAggressiveRegressor()
