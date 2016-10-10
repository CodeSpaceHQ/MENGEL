# MLTA
###### Machine Learning Test Analyzer and recorder

## Overview

### Purpose
To aid developers using machine learning algorithms in finding the best algorithms and optimal configurations for their specific situation. This is accomplished by recording as much information on a certain model as the developer wants, and then analyzing all the data to find which algorithms work best on a dataset and with what settings to they work best.

### Features
- Record results from a machine learning algorithm test
- Saves results in a Firebase Database
- (Coming Soon) View results in a WebUI
- (Coming Soon) Analyze data from results in the WebUI


### Terminology

#### Test
Unless otherwise stated, when we say test we mean a way of determining if an algorithm works. (As opposed to testing of the actual code, etc..)
#### Result Record

All the information about the test including hyper-parameters of the model used, information on the test data, results of test, etc.


## Getting Started

### Prerequisites
- [Node.js v.4.6.+](https://nodejs.org/en/)

### Installation
While each sub-module can be installed separately, we have provided a simple install script that will install all the sub-modules globally.
``` bash
./install.sh
```
While global install is preferred, if for some reason you don't want to install it globally (such as you do not have root privileges), the scripts can be run locally.

### Setup
After installing MLTA, the first thing to run is:
``` bash
mlta config
```
or if MLTA is not installed globally, navigate to '../mlta-config' and run
```bash
./mlta-config.js
```
Configuration is managed on a per person, per project basis and should be run for each project, for each user. Configuration files are stored in `~/.mlta/[PROJECT-NAME].config`

### Usage
To learn more about using MLTA, go to each sub-module you view their usage instructions.

## Sub-Modules
This module is really just a collection of sub-modules that were designed to work together to accomplish the overarching goal of finding the optimal algorithm.

### [MLTA-Config](mlta-config)
This module is for setting up your system with your project that uses MLTA. By having this handled separately from the other sub-modules, the user only has to handle authentication and other settings once as opposed to having to set it up for each sub-module individually.

### [MLTA-Record](mlta-record)
This module is for taking in all the data the user wants to save from a specific test of an algorithm and uploads it to a Firebase database.

### (Coming Soon) MLTA-Analyze
This module launches a Node.js web server for viewing and analyzing the data collected from the tests in a WebUI.
