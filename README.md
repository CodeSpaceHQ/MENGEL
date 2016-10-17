<a href="https://codeclimate.com/github/ASAAR/SE2-KaggleComp"><img src="https://codeclimate.com/github/ASAAR/SE2-KaggleComp/badges/gpa.svg" /></a> <a href="https://codeclimate.com/github/ASAAR/SE2-KaggleComp"><img src="https://codeclimate.com/github/ASAAR/SE2-KaggleComp/badges/issue_count.svg" /></a>

# SE2 Machine Learning Framework

Software Engineering 2 class kaggle competition repo. We'll also be building a bit of a framework to help make doing these easier in the future.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

What things you need in order to run this project. Detailed instructions included in "Installing".

1. A *nix system.
2. Python 2.7 (latest version), various python libraries (Scikit-learn, numpy, scipy, etc)
3. R 3.3.1 "Bug in your Hair", various R libraries
4. Javascript, NodeJS, ReactJS, among others.

### Installing
The following instructions cover setup and install of the entire system.

###### Python and Related Libraries
1. [Install the latest Python 2.7](https://www.python.org/downloads/release/python-2712/)
2. Go into your unix system and install [SciPy](https://www.scipy.org/install.html)
  1. Note that installation might be different for different systems
  2. For Ubuntu, try:
  
      ```shell
      sudo apt-get install python-numpy python-scipy python-pandas python-sympy python-nose
      ```
3. Install [SciKit-Learn](http://scikit-learn.org/stable/install.html) using pip

###### R and Related Libraries
[Install latest version of R](https://cran.r-project.org/mirrors.html)

###### Javascript, NodeJS, and Related Libraries
[Follow the instructions here, including submodules](https://github.com/ASAAR/SE2-KaggleComp/blob/master/modules/MLTA/README.md)

###### Test Data
[Download and setup the test data so that unit tests run properly](https://github.com/ASAAR/SE2-KaggleComp/blob/master/datasets/README.md)

To verify correct setup, please run the tests.

## Running the tests

Go to the top directory of the project and run the following,

```
python -m unittest discover
```

This will run tests against every module, including ones that test R and Javascript modules. It will not run all tests, but every module will be covered.

###### MLTA Testing
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
* Various packages and libraries for each language
* Firebase

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
* [template for README](https://gist.githubusercontent.com/PurpleBooth/109311bb0361f32d87a2/raw/4a39c2139c4caa4686addc1e5dd490170fb82006/README-Template.md)
