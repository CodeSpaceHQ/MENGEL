#!/usr/bin/env node

var mkdirp = require('mkdirp'); //For making the ~/.mlta folder
var path = require('path'); //Handles path naming
var prompt = require('prompt') //Gets user input
var colors = require("colors/safe"); //Makes user input pretty
var jsonfile = require('jsonfile') //Config files are in JSON format
var fs = require('fs') //fs = filesystem, used for creating files
var _ = require("underscore"); //Various useful utils. Used here to make sure the fields array are all unique

//Logging stuff
var tracer = require('tracer');
tracer.setLevel(5) //'log':0, 'trace':1, 'debug':2, 'info':3, 'warn':4, 'error':5
var logger = tracer.console({
    format: "{{timestamp}} <{{title}}> {{message}} (in {{file}}:{{line}})",
    dateformat: "HH:MM:ss.L"
});


//Other MLTA modules
var cm = require('../mlta/config-manager.js');
var fb = require('../mlta/firebase-manager');

var mltaDirPath = path.join(process.env.HOME, '.mlta'); //This basically holds this: ~/.mlta

//Used to create the MLTA home directory if it doesn't already exists. Think of bash's command 'mkdir -p'
mkdirp(mltaDirPath, function(err) {
    if(err) {
        logger.error("Unable to create MLTA folder at %s", mltaDirPath);
        return onError(err)
    }
});

//Helper function for handling errors
function onError(err) {
    logger.error('Message: %s',err.message)
    logger.error('Stack: %j', err);
    return 1;
}


//Get user input
prompt.message = ("MLTA");
prompt.delimiter = colors.green(":");
prompt.start(); //Doesn't need to be called again
prompt.get({
    properties: {
        name: {
            description: colors.magenta("Project Name:"),
            required: true,
            pattern: /^\w+$/, //The message below should give a hint as to what this pattern is
            message: 'Project name must be letters, numbers, and underscore only.'
        }
    }
}, function(err, result) {
    if(err) {
        return onError(err);
    }
    var configFileDir = path.join(mltaDirPath, result.name);
    var configFilePath = configFileDir + '.config';
    cm.getConfigIfExists(result.name, function(err, config) {
        if(err) {
            createNewConfig(result.name, configFilePath); //If that file does NOT exist, then it must be a new project
        } else {
            logger.info('Config file with name %s already exists.', result.name)
                //modifyExistConfig(result.name,configFilePath); //If that file does exist, then this is an existing project
        }
    })
});

//First try and refresh the config file from the DB, TODO: Complete this.
function modifyExistConfig(name, configFile) {
    logger.info('Loading config file for %s', name);
    var obj = jsonfile.readFileSync(configFile.toString());
    logger.debug('Loading config file: %j', obj);
}


//Get user input to create new project. This will include connecting it to firebase and creating local files for the project.
function createNewConfig(name, configFile) {
    var newConfig = new Object();
    newConfig.name = name;
    prompt.get({
        properties: {
            author: {
                description: colors.magenta("Your Name:"),
                required: true
            },
            db: {
                description: colors.magenta("Firebase Database URL:"),
                required: true
            },
            sa: {
                description: colors.magenta("Firebase Service Account JSON File Location (Please enter full path name):"),
                required: true,
                before: function(value) {
                    //Check to see if service account file exists
                    try {
                        fs.accessSync(value, fs.F_OK)
                    } catch(e) {
                        logger.error('Could not find file %s', value);
                        process.exit(1);
                    }
                    return value;
                }
            }

        }
    }, function(err, result) {
        if(err) {
            return onError(err);
        }
        newConfig.author = result.author;
        newConfig.databaseURL = result.db;
        newConfig.serviceAccount = result.sa;
        logger.info('Connecting to Firebase')
        fb.connectToFirebase(newConfig, function(err) {
            if(err) {
                return onError(err);
            }

            logger.info('Connected!');

            cm.saveConfig(newConfig, function(err) {
                if(err) {
                    return onError(err);
                } else {
                    logger.info('Configuration saved!')
                    logger.debug('Saved configuration: %j', newConfig);
                }
                process.exit();
            });
        });

    });
}
