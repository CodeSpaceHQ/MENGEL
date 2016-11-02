# This set of functions will assist in retrieving the desired models
# based on configuration options.

from os.path import dirname, basename, isfile
import glob
import setup
import sys

from modules.DMZ.models.regression import scikit_regression_learners


def get_models(prediction_type):
    models = set()

    root_path = setup.get_root_path()
    path_to_models = root_path + "/modules/DMZ/models/" + prediction_type + '/'
    sys.path.append(path_to_models)

    modules = glob.glob(dirname(path_to_models) + "/*.py")
    __all__ = [basename(f)[:-3] for f in modules if isfile(f)]

    for filename in __all__:
        importer = __import__(filename)
        for function in dir(importer):
            item = getattr(importer, function)
            if function.__str__()[0:5] == "train" and callable(item):
                models.add(item)

    return models


def find_model(model_name, prediction_type):
    root_path = setup.get_root_path()
    path_to_models = root_path + "/modules/DMZ/models/" + prediction_type + '/'
    sys.path.append(path_to_models)

    print(path_to_models)

    modules = glob.glob(dirname(path_to_models) + "/*.py")
    __all__ = [basename(f)[:-3] for f in modules if isfile(f)]

    for filename in __all__:
        importer = __import__(filename)
        for function in dir(importer):
            if function.__str__() == model_name:
                print(function.__str__())
                return function
