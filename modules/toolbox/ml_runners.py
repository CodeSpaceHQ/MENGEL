# This file has functions which call different machine learning algorithms and handle results.
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from modules.toolbox import *


# Automatically gets all regression models and runs them. This is brute force, more elegant solution to follow later.
def run_regressions(validation_pack, package):

    results = []

    for function in dir(scikit_regression_learners):
        item = getattr(scikit_regression_learners, function)
        if callable(item):

            # model is a tuple. To access the properties of the model, use model[0],
            # to get the model itself, use model[1].
            model = item()
            results.append(model_use(model[1], validation_pack, package))

    return results


# This function takes a model, the validation data, and the original data
# and either applies it to check how good the model might work, or to apply it
# to new unlabeled data.
def model_use(model, validation_pack, data_pack):
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        data_io.save_predictions(setup.get_datasets_path(), predictions, "random_forest")
