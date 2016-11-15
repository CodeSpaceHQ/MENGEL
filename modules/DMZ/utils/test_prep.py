import os
import sys

sys.path.insert(0, os.path.abspath('../../..'))
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_filler
import setup
import numpy as np
import pandas as pd


def prep_data_filler_tests_droppers(type):

    # Arrange the data
    data = fillers_setup_data()
    ratio = .99
    start = data.shape

    #Dictionary of possible inputs
    dispatcher = {"drop_rows": lambda data, ratio: data_filler.drop_missing_data_rows(data, ratio),
                  "drop_cols": lambda data, ratio: data_filler.drop_missing_data_columns(data,ratio),
                  "drop_all_rows": lambda data, _: data_filler.drop_all_missing_data_rows(data),
                  "drop_all_cols": lambda data, _: data_filler.drop_all_missing_data_columns(data)}

    end = (dispatcher[type](data,ratio)).shape

    return start, end


def prep_data_filler_tests_fillers(type):

    #Arrange the data
    data = fillers_setup_data()
    filler = 7

    if type == "fill_averages":
        data = data_filler.drop_all_missing_data_columns(data)
        data = data_filler.fill_missing_data_average(data)
    elif type == "fill_values":
        data = data_filler.fill_missing_data(data, filler)

    return data


def fillers_setup_data():
    data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")
    data["Nonsense"] = np.nan
    data = data.apply(pd.to_numeric, errors='coerce')
    data.loc[data.shape[0]] = [np.nan] * data.shape[1]
    return data
