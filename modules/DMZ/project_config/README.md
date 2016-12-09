# Project Configuration
_Handles all user input and output_

## Overview
While there are a many modules & files in this project, as a _user_, I expect there to be a single point of entry where I can go and take care of everything.
# Purpose
The purpose of this sub-module is to simplify and centralize the process of getting user input and providing the user the output of the program. The idea is simple enough:

_There will be one file that holds all the information that the user wishes/needs to provide to the program. Upon starting the program, the user will feed this file into the program. Once the program is done, this file will be updated to reflect those changes._

This sub-module holds all methods pertaining to reading in and manipulating this configuration file.
# Example
Here is an example XML file `sample_config.xml` to demonstrate all the uses of a `Configuration` object and will be used as example in the documentation below.
```XML
<MLTF-Configuration
  name="SE2-KaggleComp"
  user="asclines" >
  <Firebase
    url="FirebaseDatabaseURL"
    account="FullPathToServiceAccount"/>
  <Files>
    <Folder
      ext=".csv"
      type="test"
      path="./"
      />
    <File
      type="test"
      path="/path/to/file"/>
    <File
      type="train"
      path="/path/to/file"/>
  </Files>
  <Prediction
    target="TargetVariable"
    type="Regression"/>
  <ID_label
	   id_column="IDColumn"/>
  <Models>
    <Model name="SomeModel">
      <Param name="Param1"
        numeric="true"
        defaultValue="0"
        delta="2"
        rangeStart="0"
        rangeEnd="10" />
      <Param name="Param2"
        numeric="false"
        defaultValue="value">
        <Value> value1 </Value>
        <Value> value2 </Value>
        <Value> value3 </Value>
      </Param>
    </Model>
    <Model name="SomeModel2">
      <Param name="Param1"
        numeric="true"
        defaultValue="0"
        delta="2"
        rangeStart="0"
        rangeEnd="10" />
      <Param name="Param2"
        numeric="false"
        defaultValue="value">
        <Value> value1 </Value>
        <Value> value2 </Value>
        <Value> value3 </Value>
      </Param>
    </Model>
  </Models>
</MLTF-Configuration>
```

## Required XML elements
Below is a bare minimum XML example showing what XML elements are **required**.
```XML
<MLTF-Configuration>
  <Files/>
  <Prediction/>
  <ID_label/>
  <Models/>
</MLTF-Configuration>
```

## Required XML attributes
Below is an XML example showing the required attributes for each element.
```XML
<MLTF-Configuration
  name="SE2-KaggleComp"
  user="asclines" >
  <Firebase
    url="FirebaseDatabaseURL"
    account="FullPathToServiceAccount"/>
  <Files>
    <Folder
      type="test"
      path="./"
      />
    <File
      type="test"
      path="/path/to/file"/>
  </Files>
  <Prediction
    target="TargetVariable"
    type="Regression"/>
  <ID_label
	   id_column="IDColumn"/>
  <Models>
    <Model name="SomeModel">
      <Param name="Param1"
        numeric="true"
        defaultValue="0"
        delta="2"
        rangeStart="0"
        rangeEnd="10" />
      <Param name="Param2"
        numeric="false"
        defaultValue="value">
        <Value> value1 </Value>
        <Value> value2 </Value>
        <Value> value3 </Value>
      </Param>
    </Model>
  </Models>
</MLTF-Configuration>
```

## Features
### Configuration
There should be _one instance_ of this object throughout the life-cycle of the program.
This object is to be created by passing in the name of the configuration XML file as a constructor parameter. From there the `Configuration` object will load up the file and create itself and all its child classes as defined in the XML file. _This should be the only time in the program life-cycle that the XML file is handled._
#### Variables
The variables the program can access from this object are:
- `config_file_name`: The filepath to the input XML file passed in on construction.

- `project_name`: As defined by the attribute `name` in `<MLTF-Configuration>` attributes.

- `user_name`: As defined by the attribute `user` in `<MLTF-Configuration>` attributes.

- `config_data`: A dictionary of data from the `<MLTF-Configuration>` tag for all tags that are not `<Models>` or `<Files>` the _key_ is the tag name and the _value_ is a dictionary holding the attributes under that tag.

- `models`: A dictionary of Model objects from the `<Models>` tag where the _key_ is the name of the model and the _value_ is the `Model` object.

- `test_files`: A list of file names to be used for testing. Comes from the `<Files>` tag where the `<File>` or `<Folder>` attribute `type` equals "test".


- `train_files`: A list of file names to be used for training. Comes from the `<Files>` tag where the `<File>` or `<Folder>` attribute `type` equals "train".

#### API
- `save(filename=config_file_name)`: Saves the current configuration to XML. By default uses the same name as what was passed in.

-`prediction_target`: Returns the prediction target given in the XML file.

-`prediction_type`: Returns the prediction type given in the XML file.

-`id_column`: Returns the id column given in the XML file.



### Model
Holds all data for a Model and all methods for manipulating said data.
#### Variables
- `name`: Model name as defined by the `name` attribute in the `<Model>` tag

- `params`: A dictionary holding the parameter data as defined by the `<Params>` tags under the `<Model>` tag where the _key_ is the name of the parameter and the _value_ is the `Param` object


### Param
Holds all data for a parameter for a Model and all methods for manipulating said data.
#### Variables
- `name`: Parameter name as defined by the `name` attribute in the `<Param>` tag

- `details`: A dictionary of the parameters details as defined by the attributes under the `<Param>` tag where the _key_ is the attribute name and the _value_ is the attribute value.

- `values`: A list of values that are defined by sub-elements `<Value>` under the `<Param>` tag.
