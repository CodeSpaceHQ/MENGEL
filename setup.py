import os
import inspect


# Maybe move to framework_tools
def get_datasets_path():
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return script_dir + '/datasets/'