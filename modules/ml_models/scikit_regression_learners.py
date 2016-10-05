from sklearn import linear_model
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from modules.toolbox import framework_tools as ft
import setup


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
def train_bayesian_ridge(validation_pack, data_pack):
    # Picking model
    model = linear_model.BayesianRidge()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "bayesian_ridge")


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
def train_support_vector_regression(validation_pack, data_pack):
    # Picking model
    model = svm.SVR()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "svm_reg")


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
def train_adaboost_dtr(validation_pack, data_pack):
    # Picking model, this should be auto-selected down the road (hyperparameters)
    model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300)

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "adaboost")
