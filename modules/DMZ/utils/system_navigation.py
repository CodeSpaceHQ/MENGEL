from os.path import dirname, basename, isfile
import glob
import setup
import sys


# Returns the path to the folder with the necessary models given by the prediction type.
def path_to_models(prediction_type):
    root_path = setup.get_root_path()
    return root_path + "/modules/DMZ/models/" + prediction_type + '/'


# Adds the input path to the system path.
def add_path_to(path):
    sys.path.append(path)


# Returns the modules that are within the folder given by the path.
def get_modules(path_to_modules):
    modules = glob.glob(dirname(path_to_modules) + "/*.py")
    return [basename(f)[:-3] for f in modules if isfile(f)]
