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
- get_missing_ratios: Gets the ratio of missing values to exisiting values in a dataframe. Either operates on rows or columns depending on input. 

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
- drop_missing_data_rows: Removes any rows which have a missing to exisiting component ratio greater than desired_ratio. 
- drop_missing_data_columns: Removes any columns which have a missing to existing component ratio greater than desired_ratio. 
- drop_all_missing_data_rows: Removes any rows which hold exclusively NaN values.
- drop_all_missing_data_columns: Removes any columns which hold exclusively NaN values. 
- fill_missing_data: Replaces any NaN values within the data with the passed filler value.
  - e.g. if filler = 0, all NaNs will be replaced with 0s.
- fill_missing_data_average: Replaces any NaN values within the data with the average value of that data's column. 

This file can modify the dataset by removing rows or columns, but it cannot add either. 

### Text Handling: text_handler.py
This file is for the conversion or removal of text values from a dataset. 
- text_column_to_numeric: Takes in a dataframe column and replaces all of the text values with corresponding categorical numeric values. If given a column of nontext values, it will return the unaltered column. 
- convert_dataframe_text: Converts all text columns which have a ratio of unique components to number of components less than or equal to the desired ratio to corresponding categorical numeric data. 
- convert_nonpredictive_text: Replaces all text values in a dataframe with "NaN"s. All other data is left unchanged. 

This file can modify the dataset, but it cannot add or remove columns. 
##
This documentation is a work in progress. Please create an issue if you need something added or fork it and do a PR.
