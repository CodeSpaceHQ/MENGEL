# This is for analyzing columns or datasets, to figure out how to best act upon them.

import csv


# This will take the target "predicted" column and decide if classification or regression should be used.
def get_prediction_type(target_column):
    sorted_data = sorted(target_column)

    prediction_type = "classification"

    last = 0

    for val in sorted_data:
        if not isinstance(val, (int, float)):
            prediction_type = "invalid"
        if not last:
            last = val
        else:
            if last == val - 1:
                last = val
            elif last != val:
                prediction_type = "regression"
                break

    return prediction_type


def get_delimiter(path):
    with open(path, 'rb') as csvfile:
        return csv.Sniffer().sniff(csvfile.read(), delimiters=';,').delimiter
