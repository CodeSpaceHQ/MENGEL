#!/usr/bin/env node
var mkdirp = require('mkdirp'); //For making the ~/.mlta folder
var path = require('path'); //Handles path naming
var prompt = require('prompt') //Gets user input
var colors = require("colors/safe"); //Makes user input pretty
var jsonfile = require('jsonfile') //Config files are in JSON format
var fs = require('fs') //fs = filesystem, used for creating files
var _ = require("underscore"); //Various useful utils. Used here to make sure the fields array are all unique

var mltaDirPath = path.join(process.env.HOME, '.mlta'); //This basically holds this: ~/.mlta

//Used to create the MLTA home directory if it doesn't already exists. Think of bash's command 'mkdir -p'
mkdirp(mltaDirPath, function(err){
  if (err) {
    console.error(err);
    process.exit(1);
  }
});

//Helper function for handling errors
function onError(err){
  console.log(err);
  return 1;
}

//Helper function for logging
function log(message){
  console.log(message);
}

//Get user input
prompt.message = ("MLTA");
prompt.start(); //Doesn't need to be called again
prompt.get({
  properties: {
    name: {
      description: colors.magenta("Project Name:"),
      pattern:  /^\w+$/, //The message below should give a hint as to what this pattern is
      message: 'Project name must be letters, numbers, and underscore only.'
    }
  }
}, function (err, result) {
  if(err){return onError(err);}
  //Config files are created and stored as [Project-Name].config
  var configFileDir = path.join(mltaDirPath,result.name);
  var configFilePath = configFileDir+'.config';
  fs.access(configFilePath, fs.F_OK, function(err) {
    if (err) {
      createNewConfig(result.name,configFilePath);//If that file does NOT exist, then it must be a new project
    } else {
      modifyExistConfig(result.name,configFilePath); //If that file does exist, then this is an existing project
    }
  });
});

//First try and refresh the config file from the DB, TODO: Complete this.
function modifyExistConfig(name,configFile){
  log("Loading configuration for " + name);
  var obj = jsonfile.readFileSync(configFile.toString());
  log(obj.name)
}


//Get user input to create new project. This will include connecting it to firebase and creating local files for the project.
function createNewConfig(name,configFile){
  var newConfig = new Object();
  newConfig.name = name;
  prompt.get({
    properties: {
      author: {
        description: colors.magenta("Your Name:")
      },
      url: {
        description: colors.magenta("Firebase URL:")
      },
      auth: {
        description: colors.magenta("Auth:")
      }
    }
  }, function(err, result){
    if(err){return onError(err);}
    newConfig.author = result.author;
    newConfig.url = result.url;
    newConfig.auth = result.auth;
    newConfig.models = [];

    function addModelDef(){
      prompt.get({
        properties:{
          yn: {
            description: colors.magenta("Add a model definition?[y/n]"),
            pattern: '^[y,n]',
            message: '[y]es or [n]o.'
          }
        }
      }, function(err, result){
        if(result.yn == 'n'){
          jsonfile.writeFileSync(configFile,newConfig);
        } else if(result.yn == 'y'){
          createNewModel(//);
          function(errror,model){
            newConfig.models.push(model);
            addModelDef();
          });
        } else { //Just in case regex doesn't work above for any reason
          addModelDef();
        }

      });
    };

    addModelDef();

  });
}

function createNewModel(callback){
  prompt.get({
    properties: {
      name : {
        description: colors.magenta("Model Name:"),
        pattern: /^\w+$/,
        message: 'Model name must be letters, numbers, and underscore only.'
      },
      fields : {
        description: colors.magenta("Enter required fields, seperated by commas: "),
        pattern: '^[a-zA-Z0-9_]+(,[a-zA-Z0-9_]+)*$',
        message: 'Field names can only contain (a-z,A-Z,0-9,_) and must be seperated by a comma'
      }
    }
  },
    function(err, result){
      if(err){return onError(err);}
      model = new Object();
      model.name=result.name;
      model.fields=_.uniq(result.fields.split(','));
      callback(null,model);
    });
}
