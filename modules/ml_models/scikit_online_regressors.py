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
    model = linear_model.SGDRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "sgd_regressor")


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
def train_passive_aggressive_regressor(validation_pack, data_pack):
    # Picking model
    model = linear_model.PassiveAggressiveRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "pa_regressor")
