import sys
import os

sys.path.insert(0, '/modules/toolbox')

import csv_splitter

def csv_setup():
    script_dir = os.path.dirname(__file__)
    total_file_path = script_dir + '/data/'
    
    csv_splitter.setup_split(total_file_path, 'train_categorical.csv')
    csv_splitter.setup_split(total_file_path, 'train_date.csv')
    csv_splitter.setup_split(total_file_path, 'train_numeric.csv')

    open(total_file_path + 'split.txt', 'w')

csv_setup()
