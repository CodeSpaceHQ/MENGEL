#!/usr/bin/env node
var program = require('commander');
var jsonfile = require('jsonfile') //Config files are in JSON format
var fs = require('fs') //fs = filesystem, used for creating files
var path = require('path'); //Handles path naming

var fb = require('../utils/firebase-manager.js')

//Helper function for logging
function log(message){
  console.log(message);
}

function modelData(val, data) {
  var info = val.split(':');
  var pair = {};
  data[info[0]] = info[1];
  return data;
}


function testData(val, data){
  var info = val.split(':');
  var pair = {};
  data[info[0]] = info[1];
  return data;
}

//Get arguemnts/options
program
  .version('0.0.1')
  .option('-p, --project <name>', 'Name of project.')
  .option('-l, --label <label>' , 'Used to identify specific models for future reference. ')
  .option('-m, --modelType <type>' , 'Type of model used.')
  .option('-d, --modelData <key:value>' , 'Key-value pair of info about the model', modelData , {})
  .option('-D, --testData < key:value>' , 'Key-value pair of info about the test', testData , {})
  .parse(process.argv);

//Make sure all required arguments have been met and that all optional arguemnts that were not passed in have their default values set
  if(!program.project){
    console.log("Project name must be specified.")
    process.exit();
  }

  if(!program.label){
      console.log("No label added");
      program.label = '';
  }

  if(!program.modelType){
    console.log("Model type must be specified");
    process.exit();
  }

var configFileDir = path.join(process.env.HOME, '.mlta',program.project);
var configFile = configFileDir+'.config';

fs.access(configFile, fs.F_OK, function(err) {
  if(err){
    log("Error: Could not load config file for " + program.project);
    process.exit();
  }

  var config =  jsonfile.readFileSync(configFile.toString());
  console.log('Config = %j', config);

  fb.connectToFirebase(config,function(err){
    if(err){
      console.log(err);
      process.exit();
    }

    console.log("Connected!");

    var result = {
      label: program.label,
      createdAt: new Date().toJSON(),
      author: config.author,
      modelType: program.modelType,
      modelData: program.modelData,
      testData: program.testData

    };

    fb.saveResult(result, function(err){
      if(err){
        console.log("Error: %s", err);
      } else {
        console.log("Results saved");
      }``
      process.exit();
    });
  });

});





//Validate arguments/options
