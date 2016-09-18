import os
import inspect

import modules.ml_models.scikit_online_learners as online_ml
import modules.toolbox.csv_splitter as csv_split

def csv_setup():
    total_file_path = get_datasets_path()

    csv_split.setup_split(total_file_path, 'train_categorical.csv')
    csv_split.setup_split(total_file_path, 'train_date.csv')
    csv_split.setup_split(total_file_path, 'train_numeric.csv')

    open(total_file_path + 'split.txt', 'w')

def get_datasets_path():
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return script_dir + '/datasets/'
