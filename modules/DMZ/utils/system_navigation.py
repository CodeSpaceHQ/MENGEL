from os.path import dirname, basename, isfile
import glob
import setup
import sys


def path_to_models(prediction_type):
    root_path = setup.get_root_path()
    return root_path + "/modules/DMZ/models/" + prediction_type + '/'


def add_path_to(path):
    sys.path.append(path)


def get_modules(path_to_modules):
    modules = glob.glob(dirname(path_to_modules) + "/*.py")
    return [basename(f)[:-3] for f in modules if isfile(f)]
