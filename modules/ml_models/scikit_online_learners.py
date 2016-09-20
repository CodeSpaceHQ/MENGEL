from sklearn import linear_model
from modules.toolbox import framework_tools as ft

#
# There is also some repetitive code in terms of fitting and scoring models, this will
# likely be split out into a new helper
#

def run_sgd_regressor(path, filename):
    x_train, x_test, y_train, y_test = ft.get_train_test(path, filename)

    # Picking model
    model = linear_model.SGDRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(x_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test)


def run_passive_aggressive_regressor(path, filename):
    x_train, x_test, y_train, y_test = ft.get_train_test(path, filename)

    # Picking model
    model = linear_model.PassiveAggressiveRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(x_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test)

