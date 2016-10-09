# MLTA Config
###### Machine Learning Test Analyzer and recorder Configuration
The MLTA Config tool is used to create and manage your MLTA configurations. By having this handled separately from the other sub-modules, the user only has to handle authentication and other settings once as opposed to having to set it up for each of the other sub-modules individually.

## Getting Started

### Prerequisites
- [Node.js v.4.6.+](https://nodejs.org/en/)
- [Firebase](https://firebase.google.com)

### Installation
If you didn't choose to install using the install script found [here](../mlta#installation), you can install with this command
```bash
npm install -g
```
The `-g` flag installs mlta-config globally so you can call this program from anywhere. However, if you do not want to or cannot install globally `npm install` will work, you just will have to call mlta-config from this directory.

 so you can use the command `mlta config`. However, if you do not or cannot install globally `npm install` will work and to call the program you will have to use `./mlta-config.js` instead of `mlta config`.


### Usage
If you installed globally, you can launch the MLTA Configuration tool with this command:
```bash
mlta config
```
However, if you didn't then you will have to navigate to this directory and run `./mlta-config.js`.

## Add a New Project
### Setting up Firebase
Before running this program, make sure your Firebase is ready. MLTA acts as a server as far as Firebase is concerned when it comes to connecting to Firebase. Go [here](https://firebase.google.com/docs/server/setup) and follow the instructions to setup your Firebase to interact with a server.
When done, make sure you have the JSON file with your service account credentials saved to your computer. You will be needing the path to that JSON file and the URL to the database below.

### Setting up your computer
To add a new project to your configuration so that you may either save results to the project's Firebase Database or launch the WebUI to anazlyze the data in the project's Firebase Database, simply start the program and follow the on screen commands.
```bash

$ mlta config
MLTA:Project Name:: MyProjectsName
MLTA:Your Name:: MyName
MLTA:Firebase Database URL:: MyDatabaseURL
MLTA:Firebase Service Account JSON File Location (Please enter full path name):: FullPathTOServiceAccount

```

- Project Name: Case sensitive name that is used to refer to your project from other sub-modules. By simply passing in the project name, the other sub-modules can get all the information they need from the configuration to do what they need to do.

- Your Name: This is the field that is used to fill the 'author' field in test records that appear on the database. This is used to see who uploaded the record for easier filtering of data on the WebUI.

- Database URL: The URL from above where you set up Firebase.

- Firebase Service Account JSON File Location: The *exact* file location of the service account JSON file that you got from above where you set up Firebase. By *exact* we mean **no relative paths** using `~/` etc..


If all went well, a configuration file for your project has been created and stored in `~/.mlta/`.
Now all the MLTA sub-modules can do their thing.


## (Coming Soon) Modify Existing Project Configuration
