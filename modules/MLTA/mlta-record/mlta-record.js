#!/usr/bin/env node

var program = require('commander');
var jsonfile = require('jsonfile') //Config files are in JSON format
var fs = require('fs') //fs = filesystem, used for creating files
var path = require('path'); //Handles path naming

var placeholderKey = "1234"; //When the data is only being validated, not uploaded, this is the key that is returned.

//Logging stuff
var tracer = require('tracer');
tracer.setLevel(4) //'log':0, 'trace':1, 'debug':2, 'info':3, 'warn':4, 'error':5
var logger = tracer.console({
    format: "{{timestamp}} <{{title}}> {{message}} (in {{file}}:{{line}})",
    dateformat: "HH:MM:ss.L"
});


var fb = require('../mlta/firebase-manager');

//Helper function for handling errors
function onError(err) {
    console.log(1)
    logger.error('Message: %s',err.message)
    logger.debug('Stack: %j', err);
    return 1;
}

function modelData(val, data) {
    var info = val.split(':');
    var pair = {};
    data[info[0]] = info[1];
    return data;
}


function testData(val, data) {
    var info = val.split(':');
    var pair = {};
    data[info[0]] = info[1];
    return data;
}

//Get arguemnts/options
function validateOptions(program, done) {
  logger.debug("Program: %j",program);
    var options = new Object();
    //Make sure all required arguments have been met and that all optional arguemnts that were not passed in have their default values set
    if(!program.project) {
        return done(new Error('Project name must be specified.'));
    }
    options.project = program.project;

    if(!program.label) {
        logger.info('No label added.');
        options.label = '';
    } else {
        options.label = program.label;
    }

    if(!program.modelType) {
        return done(new Error('Model type must be specified.'));
    }
    options.modelType = program.modelType;

    options.modelData = program.modelData;
    options.testData = program.testData;

    done(null, options);
}


function saveRecordToFB(options, done) {

    logger.debug('Options: %j', options);
    var configFileDir = path.join(process.env.HOME, '.mlta', options.project);
    var configFile = configFileDir + '.config';
    fs.access(configFile, fs.F_OK, function(err) {
        if(err) {
            logger.info("Error: Could not load config file for %s",options.project);
            return done(new Error("Could not load config file for " + options.project));
        }

        var config = jsonfile.readFileSync(configFile.toString());
        logger.debug('Config: %j', config);

        fb.connectToFirebase(config, function(err) {
            if(err) {
                return done(err);
            }
            logger.info('Connected to Firebase!');

            var result = {
                label: options.label,
                createdAt: new Date().toJSON(),
                author: config.author,
                modelType: options.modelType,
                modelData: options.modelData,
                testData: options.testData

            };

            fb.saveResult(result, function(err,key) {
                if(err) {
                    return done(err);
                } else {
                    console.log("0")
                    console.log(key)
                    return done(null);
                }
            });
        });

    });
}

program
    .version('0.0.1')
    .option('-p, --project <name>', 'Name of project.')
    .option('-l, --label <label>', 'Used to identify specific models for future reference. ')
    .option('-m, --modelType <type>', 'Type of model used.')
    .option('-d, --modelData <key:value>', 'Key-value pair of info about the model', modelData, {})
    .option('-D, --testData < key:value>', 'Key-value pair of info about the test', testData, {})
    .option('-v  --validate','Validate input only, does not upload to database')
    .parse(process.argv);


validateOptions(program, function(err, options) {
    if(err) {
        return onError(err);
    }
    logger.info('onValidOptionsDone');
    logger.debug('Options: %j', options);
    if(!program.validate){
      saveRecordToFB(options, function(err) {
          logger.info('saved to firebase');
          if(err) return onError(err);
          process.exit();
      });
    } else {
      console.log("0")
      console.log("%s",placeholderKey) //Place holder key
    }

});
