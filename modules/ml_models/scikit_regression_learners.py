from sklearn import linear_model
from sklearn import svm
from modules.toolbox import framework_tools as ft
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
def run_bayesian_ridge(path, filename, separator):
    x_train, x_test, y_train, y_test = ft.get_train_test(path, filename, separator)

    # Picking model
    model = linear_model.BayesianRidge()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(x_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test)


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
def run_support_vector_regression(path, filename, separator):
    x_train, x_test, y_train, y_test = ft.get_train_test(path, filename, separator)

    # Picking model
    model = svm.SVR()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(x_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test)


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
def run_adaboost_dtr(path, filename, separator):
    x_train, x_test, y_train, y_test = ft.get_train_test(path, filename, separator)

    # Picking model, this should be auto-selected down the road (hyperparameters)
    model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300)

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(x_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(x_test, y_test)
