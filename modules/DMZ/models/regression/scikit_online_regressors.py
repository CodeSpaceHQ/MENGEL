from sklearn import linear_model
from modules.DMZ.models import model_properties as mp

#
# There is also some repetitive code in terms of fitting and scoring models, this will
# likely be split out into a new helper
#


# "Linear model fitted by minimizing a regularized empirical loss with SGD"
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor
def train_sgd_regressor():
    # Picking model
    return mp.ModelProperties(regression=True, online=True), linear_model.SGDRegressor()


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
def train_passive_aggressive_regressor():
    # Picking model
    return mp.ModelProperties(regression=True, online=True), linear_model.PassiveAggressiveRegressor()
