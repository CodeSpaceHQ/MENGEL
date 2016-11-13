# Project Configuration
_ Handles all user input and output _

## Overview
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
    <File
      type="train"
      path="/path/to/file"/>
    <File
      type="train"
      path="/path/to/file"/>
  </Files>
  <Prediction
    target="TargetVariable"
    type="Regression"/>
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
## Features
### Configuration
There should be _one instance_ of this object throughout the life-cycle of the program.
This object is to be created by passing in the name of the configuration XML file as a constructor parameter. From there the `Configuration` object will load up the file and create itself and all its child classes as defined in the XML file. _This should be the only time in the program life-cycle that the XML file is handled._
#### Variables
The variables the program can access from this object are:
- `project_name`: As defined by the attribute `name` in `<MLTF-Configuration>` attributes.

- `user_name`: As defined by the attribute `user` in `<MLTF-Configuration>` attributes.

- `config_data`: A dictionary of data from the `<MLTF-Configuration>` tag for all tags that are not `<Models>` or `<Files>` the _key_ is the tag name and the _value_ is a dictionary holding the attributes under that tag.

- `models`: A dictionary of Model objects from the `<Models>` tag where the _key_ is the name of the model and the _value_ is the `Model` object.

- `test_files`: A list of file names to be used for testing. Comes from the `<Files>` tag where the `<File>` attribute `type` equals "test".


- `train_files`: A list of file names to be used for training. Comes from the `<Files>` tag where the `<File>` attribute `type` equals "train".


### Model
Holds all data for a Model and all methods for manipulating said data.
#### Variables
- `name`: Model name as defined by the `name` attribute in the `<Model>` tag

- `params`: A dictionary holding the parameter data as defined by the `<Params>` tags under the `<Model>` tag where the _key_ is the name of the parameter and the _value_ is the `Param` object
