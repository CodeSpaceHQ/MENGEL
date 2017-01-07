import os
import inspect


# Maybe move to framework_tools
def get_datasets_path():
    return get_root_path() + '/datasets/'


def get_root_path():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
