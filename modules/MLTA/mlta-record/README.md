# MLTA Config
###### Machine Learning Test Analyzer and recorder Configuration
The MLTA Record tool is used to create records of machine learning algorithm tests and store the results in a Firebase database.

## Getting Started
### Before You Begin
Make sure you have properly [installed MLTA Config](../mlta-config#installation) and [added your project](../mlta-config#add-a-new-project)

### Installation
If you didn't choose to install using the install script found [here](../#installation), you can install with this command
```bash
npm install -g
```
The `-g` flag installs `mlta record` globally so you can call this program from anywhere. However, if you do not want to or cannot install globally `npm install` will work, you just will have to call mlta-record from this directory.

 so you can use the command `mlta record`. However, if you do not or cannot install globally `npm install` will work and to call the program you will have to use `./mlta-record.js` instead of `mlta record`.


 ### Usage
 If you installed globally, you can launch the MLTA Record tool with this command:
 ```bash
 mlta record
 ```
 However, if you didn't then you will have to navigate to this directory and run `./mlta-record.js`.
```bash
Usage: mlta-record [options]

Options:

  -h, --help                   output usage information
  -V, --version                output the version number
  -p, --project <name>         Name of project.
  -l, --label <label>          Used to identify specific models for future reference.
  -m, --modelType <type>       Type of model used.
  -d, --modelData <key:value>  Key-value pair of info about the model
  -D, --testData < key:value>  Key-value pair of info about the test
```


## Example
Suppose we are testing a neural net on some data. Maybe we are testing some [wine quality](https://archive.ics.uci.edu/ml/datasets/Wine+Quality).

Things we might want to keep track of are:
- Training data file name ("winetraindata1.csv")
- How many entries were in the training data (200)
- Testing data file name ("winetestdata1.csv")
- How many entries were in the training data (800)
- Which variable was being predicted (quality )
- Which variables were used to predict (density,sulphates)
- Size of the hidden layer of the neural net (3)
- What percentage of the testing data did the neural net get correct with these parameters. (80)

We can use the `mlta record` CLI tool to record this data as follows:
```bash
./mlta-record.js  -p PROJECTNAME  -l WineNNetTest1 -m nnet -d hiddensize:3 -d predict:quality -d predicters:density,sulphates -D testfile:winetestdata1.csv -D trainfile:winetraindata1.csv -D testentries:200 -D trainentries:800 -D score:80
```

and in Firebase, the JSON entry would look like this:
```JSON
{
  "author" : "alexander",
  "createdAt" : "2016-10-09T19:10:02.520Z",
  "label" : "WineNNetTest1",
  "modelData" : {
    "hiddensize" : "3",
    "predict" : "quality",
    "predicters" : "density,sulphates"
  },
  "modelType" : "nnet",
  "testData" : {
    "score" : "80",
    "testentries" : "200",
    "testfile" : "winetestdata1.csv",
    "trainentries" : "800",
    "trainfile" : "winetraindata1.csv"
  }
}
```

Now, the CLI command was pretty ugly. It was not designed to be pretty, it was designed for flexibility, so that no matter what programming language the user is using and no matter the algorithm, `mlta record` could handle it. However, we understand that this is not convenient and that is why we are working on wrappers in other languages that can be included into your source code so you don't have to handle the CLI command.

## (Coming Soon) API
Currently, the API's under development are
- An R module
- A Python Module
