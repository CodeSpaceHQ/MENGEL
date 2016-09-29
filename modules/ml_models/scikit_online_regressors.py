from sklearn import linear_model
from modules.toolbox import framework_tools as ft

#
# There is also some repetitive code in terms of fitting and scoring models, this will
# likely be split out into a new helper
#


# "Linear model fitted by minimizing a regularized empirical loss with SGD"
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor
def train_sgd_regressor(x_train, y_train):
    # Picking model
    model = linear_model.SGDRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    return model.fit(x_train, y_train)


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
def train_passive_aggressive_regressor(x_train, y_train):
    # Picking model
    model = linear_model.PassiveAggressiveRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    return model.fit(x_train, y_train)
