# Usage and Purpose Documentation
This file will provide instructions on how to use and modify the files in this folder.

### Dataset Insight: dataset_insight.py
The purpose of this file is finding information that is key to understanding how to operate on a dataset.
- get_delimiter
  - This function is important because it takes the complete path to a file and returns the delimiter used
  in that file.
- get_prediction_type
  - This function is a naive method of finding out if classification or regression should be used on a dataset.
  Isaac is not happy with the way it works, so it's currently not used and the system will force the user to
  give regression or classification.

This file should only have functions that information about a dataset. None of the functions in here should
modify the dataset.

### Data Splitting: data_splitting.py
The purpose of this file is to split a dataset into portions or remove a section of that dataset based on some need
elsewhere.
- get_train_test: This function splits a dataset into training and testing sets for x and y.
- separate_target: This function removes the target column or "label" from the dataset for proper training.

This file should not modify the data, only separate out portions of it.

### Data IO: data_io.py
This file governs loading and saving of data. It currently supports CSV files, but will later support other formats.
- get_data: Loads data from a csv file.
- save_predictions: Saves predictions provided by a model to a csv file.

This file should not modify the dataset, only load or save it.

### Data Prepping: data_prepping.py
This file is for modification of data, such as scaling or filling in missing data.
- scale_numeric_data: Centers the target data before scaling to unit variance. Note that it ignores non-numeric
columns in the dataset.

This file can modify the dataset, but it should not add or remove columns.

### Data Filling: data_filler.py
This file is for the removal or replacement of values of data which are missing.
- drop_missing_data_rows: Removes any rows which have fewer than threshold non NaN values.
- drop_missing_data_columns: Removes any columns which have fewer than threshold non NaN values.
- drop_all_missing_data_rows: Removes any rows which hold exclusively NaN values.
- drop_all_missing_data_columns: Removes any columns which hold exclusively NaN values. 
- fill_missing_data: Replaces any NaN values within the data with the passed filler value.
- fill_missing_data_average: Replaces any NaN values within the data with the average value of that data's column. 

This file can modify the dataset by removing rows or columns, but it cannot add either. 

##
This documentation is a work in progress. Please create an issue if you need something added or fork it and do a PR.