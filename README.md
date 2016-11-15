<a href="https://codeclimate.com/github/ASAAR/SE2-KaggleComp"><img src="https://codeclimate.com/github/ASAAR/SE2-KaggleComp/badges/gpa.svg" /></a> <a href="https://codeclimate.com/github/ASAAR/SE2-KaggleComp"><img src="https://codeclimate.com/github/ASAAR/SE2-KaggleComp/badges/issue_count.svg" /></a>

# Machine Learning Framework
This project is an effort to create a framework that automates basic machine learning and will help a team quickly get some results and an idea of what algorithms might be useful. It is **not** a replacement for custom built systems that leverage machine learning.

## Overview

### Purpose
To aid developers using machine learning algorithms in finding the best algorithms and optimal configurations for their specific situation. This is accomplished by recording as much information on a certain model as the developer wants, and then analyzing all the data to find which algorithms work best on a dataset and with what settings to they work best.

### Features
- Automatically applies several of a number of machine learning algorithms against the input data based on the settings it is given
- Has a large number of tests that make sure algorithms included still run and haven't become outdated
- Can be put in validation or application mode (train/test mode)
- Record results from a machine learning algorithm test
- Saves results in a Firebase Database
- (Coming Soon) View results in a WebUI
- (Coming Soon) Analyze data from results in the WebUI

### Terminology

#### Test
Unless otherwise stated, when we say test we mean a way of determining if an algorithm works. (As opposed to testing of the actual code, etc..)

#### Test Data
Test data is data that is unlabeled, in other words it does not have a column or label which represents the target that a model is trying to predict. So if a model predicts housing prices, "test data" will not have the housing prices listed.

#### Train Data
Training data on the other hand does have the target column, because the model has to use that column to be trained.

#### Result Record

All the information about the test including hyper-parameters of the model used, information on the test data, results of test, etc.

## Getting Started

These instructions will get you a copy of the entire project up and running on your local machine for development and testing purposes. If you wish to deploy submodules individually, please see the instructions for that specific module. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

What things you need in order to run this project. Detailed instructions included in "Installing".

1. A *nix system.
2. Python 2.7 (latest version), various python libraries (Scikit-learn, numpy, scipy, etc)
3. R 3.3.1 "Bug in your Hair", various R libraries
4. Javascript, NodeJS, ReactJS, among others.

### Installing
The following instructions cover setup and install of the entire system.

#### Python and Related Libraries
1. [Install the latest Python 2.7](https://www.python.org/downloads/release/python-2712/)
2. Go into your unix system and install [SciPy](https://www.scipy.org/install.html)
  1. Note that installation might be different for different systems
  2. For Ubuntu, try:

      ```shell
      sudo apt-get install python-numpy python-scipy python-pandas python-sympy python-nose
      ```
3. Install [SciKit-Learn](http://scikit-learn.org/stable/install.html) using pip

#### R and Related Libraries
1. [Install latest version of R](https://cran.r-project.org/mirrors.html)
2.  Install R packages

        R
        install.packages("dplyr")
        install.packages("rpart")
        install.packages("C50")
        install.packages("stats")
        q()


#### Javascript, NodeJS, and Related Libraries
[Follow the instructions here, including submodules](modules/MLTA/README.md)

#### Test Data
[Download and setup the test data so that unit tests run properly](datasets/README.md)

To verify correct setup, please run the tests.

## Running the tests

Go to the top directory of the project and run the following,

```
python -m unittest discover
```

This will run tests against every module, including ones that test R and Javascript modules. It will not run all tests, but every module will be covered.

### MLTA Testing
Documentation pending

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests
We measure code quality with CodeClimate, to see that data go [here](https://codeclimate.com/github/ASAAR/SE2-KaggleComp).

## Deployment
Pending

## Built With

* Bash on Ubuntu on Windows
* Pycharm
* Python, Javascript, R
* Firebase

###### Libraries, Frameworks, and Packages Used
- Python: Scikit-learn, scipy, pandas, numpy
- R: dplyr
- Javascript: NodeJS

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We do not use versioning currently, we will likely use [SemVer](http://semver.org/) for versioning eventually. For the versions available, see the [tags on this repository](https://github.com/ASAAR/SE2-KaggleComp/tags).

## Authors

* **Alexander Clines** - *Initial work* - [asclines](https://github.com/asclines)
* **Isaac Griswold-Steiner** - *Initial work* - [ASAAR](https://github.com/ASAAR)
* **Zakery Fyke** - *Initial work* - [ZakeryFyke](https://github.com/ZakeryFyke)
* **Ryan McBerg** - *Initial work* - [RyanMcBerg](https://github.com/RyanMcBerg)

See also the list of [contributors](https://github.com/ASAAR/SE2-KaggleComp/graphs/contributors) who participated in this project.

## License
We haven't dealt with licensing yet.

## Acknowledgements

* Hat tip to anyone whose code was used
* [template for README](https://gist.githubusercontent.com/PurpleBooth/109311bb0361f32d87a2/raw/4a39c2139c4caa4686addc1e5dd490170fb82006/README-Template.md)
* The labels used in the issues section were inspired by [this site](https://robinpowered.com/blog/best-practice-system-for-organizing-and-tagging-github-issues/)
