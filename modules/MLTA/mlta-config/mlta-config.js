#!/usr/bin/env node
var mkdirp = require('mkdirp'); //For making the ~/.mlta folder
var path = require('path'); //Handles path naming
var prompt = require('prompt') //Gets user input
var colors = require("colors/safe"); //Makes user input pretty
var jsonfile = require('jsonfile') //Config files are in JSON format
var fs = require('fs') //fs = filesystem, used for creating files
var _ = require("underscore"); //Various useful utils. Used here to make sure the fields array are all unique
var firebase = require("firebase"); //For Firebase stuff..duh..

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
prompt.delimiter = colors.green(":");
prompt.start(); //Doesn't need to be called again
prompt.get({
  properties: {
    name: {
      description: colors.magenta("Project Name:"),
      required: true,
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
  log(obj);
}


//Get user input to create new project. This will include connecting it to firebase and creating local files for the project.
function createNewConfig(name,configFile){
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
        before: function(value){
          //Check to see if service account file exists
          try{
            fs.accessSync(value, fs.F_OK)
          } catch(e){
            log("Could not find file: " + value);
            process.exit(1);
          }
          return value;
        }
      }

    }
  }, function(err, result){
    if(err){return onError(err);}
    newConfig.author = result.author;
    newConfig.databaseURL = result.db;
    newConfig.serviceAccount = result.sa;

    connectToFirebase(newConfig,configFile);
  });
}


//Handles initializing firebase and checking authentication.
function connectToFirebase(mltaConfig,configFilePath){
  log("Connecting to Firebase")
  var fbConfig = {
    serviceAccount: mltaConfig.serviceAccount,
    databaseURL: mltaConfig.databaseURL
  };
  firebase.initializeApp(fbConfig);
   var db = firebase.database();

   //If we don't have a connection in a few seconds, whether its due to incorrect credintials, or network error, we cannot continue.
   var connFailTimeout = setTimeout(function() {
     console.log('Failed to connect to Firebase.');
     process.exit(); //Bye-bye!
   }, 10000);

   //Called if we have an established, authorized connection to the Firebase database
  function ready() {
    clearTimeout(connFailTimeout); //We've connected to lets go ahead and tell the connFailTimeout dude up there ^ that he can leave his post.
    log("Connected!");

    //We have now verified that the info the user gave us was legit. Let's write it to the config file.
    jsonfile.writeFile(configFilePath,mltaConfig,function(err){
      if(err){return onError(err)}
      log("Configuration saved!");
      process.exit();
    });
  };

  /*
    The connection function
    meets at the internet junction
    to make a conjunction
    or an adjunction
    unless theres an injunction
    to which we disfunction
    and ends with expunction.
  */
  var connFunc = db.ref('.info/connected').on('value', function(s) {
    if(s.val() === true) {
      db.ref('.info/connected').off('value', connFunc);
      ready();
    }
  });

}
