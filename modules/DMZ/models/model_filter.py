# This set of functions will assist in retrieving the desired models
# based on configuration options.

from modules.DMZ.utils import system_navigation as sn


# Gets all of the models that are compatible with the prediction type.
# Input:
# - prediction_type: "regression" or "classification"
# Output:
# - Functions that can be called and return the model along with the properties that
# the model has.
def get_models(prediction_type):
    models = set()

    sn.add_path_to(sn.path_to_models(prediction_type))
    modules = sn.get_modules(sn.path_to_models(prediction_type))

    for filename in modules:
        importer = __import__(filename)
        for function in dir(importer):
            item = getattr(importer, function)
            if function.__str__()[0:5] == "train" and callable(item):
                models.add(item)

    return models
