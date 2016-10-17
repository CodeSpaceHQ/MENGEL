# MLTA API
###### Machine Learning Test Analyzer and recorder Python API

# Overview
Provides a Python wrapper over the 'mlta-record' command line call.
Allows the developer to easily include MLTA Record into their Python project while at the same time providing error handling for 'mlta-record'.

**Note: For this API to work, MLTA must have been installed globally.**

# Usage
Since this Python file uses MLTA's global commands, it can be placed anywhere. So go ahead and copy the `mlta` file anywhere you want, or just include it from this folder here (that way you can get updates). Whatever works best for * you. *

## Example Usage
```python
from mlta import record # One of several ways you can import this file

# Create project and record
example_project = record.Project("Example_Project")
example_record = record.ResultRecord("Example_Model_Type")

# Add model data to the record
example_record.add_model_data_pair("model_key1","model_val1")
example_record.add_model_data_pair("model_key3","model_val2")
example_record.add_model_data_pair("model_key2","model_val3")

# Add test data to the record
example_record.add_test_data_pair("test_key","test_val")

# Add record to the project
example_project.add_record(example_record)

# Save all records added to the project
example_project.save_all_records()

```



# API
## Project
- Create a new project with `name` matching the project name used to configuring project
```python
__init__(self,name)
```
- Adding a ResultRecord
```python
add_record(self,record)
```
- Saving all records to Firebase (preferred way to save records)
```python
save_all_records(self)
```
- Saving an individual record to Firebase (if for some reason you do not want to save all the records). Returns the UID generated for this record.
```python
save_record(record)
```

## ResultRecord
- Create a new record. All ResultRecords require a model type.
```python
__init__(self,model_type)
```

- Add model data key, value pair to record
```python
add_model_data_pair(self, key, value)
```

- Add test data key, value pair to record
```python
add_test_data_pair(self, key, value)
```
