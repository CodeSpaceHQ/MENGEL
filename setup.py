import sys
import os

sys.path.insert(0, '/modules/toolbox')
sys.path.insert(0, '/modules/ml_models')

import modules.ml_models.scikit_online_learners as online_ml
import modules.toolbox.csv_splitter as csv_split

def csv_setup():
    script_dir = os.getcwd() # Compatible with Linux and Windows
    total_file_path = script_dir + '/datasets/'

    csv_split.setup_split(total_file_path, 'train_categorical.csv')
    csv_split.setup_split(total_file_path, 'train_date.csv')
    csv_split.setup_split(total_file_path, 'train_numeric.csv')

    open(total_file_path + 'split.txt', 'w')

def test_online_learners():
    script_dir = os.getcwd() # Compatible with Linux and Windows
    total_file_path = script_dir + '/datasets/'

    online_ml.run_SGDRegressor(total_file_path, "winequality-red.csv")

test_online_learners()