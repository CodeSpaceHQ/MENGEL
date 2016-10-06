from sklearn import linear_model
import setup
from modules.toolbox import framework_tools as ft

#
# There is also some repetitive code in terms of fitting and scoring models, this will
# likely be split out into a new helper
#


# "Linear model fitted by minimizing a regularized empirical loss with SGD"
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor
def train_sgd_regressor(validation_pack, data_pack):
    # Picking model
    return linear_model.SGDRegressor()


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
def train_passive_aggressive_regressor(validation_pack, data_pack):
    # Picking model
    return linear_model.PassiveAggressiveRegressor()
