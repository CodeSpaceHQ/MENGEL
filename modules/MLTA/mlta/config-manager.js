#!/usr/bin/env node
var path = require('path'); //Handles path naming
var fs = require('fs') //fs = filesystem, used for creating files
var jsonfile = require('jsonfile') //Config files are in JSON format

var mltaDirPath = path.join(process.env.HOME, '.mlta'); //This basically holds this: ~/.mlta

var exports = module.exports = {};

//Returns error if config does not exists
exports.getConfigIfExists = function(name,done){
  //Config files are created and stored as [Project-Name].config
  var configFileDir = path.join(mltaDirPath,name);
  var configFilePath = configFileDir+'.config';
  fs.access(configFilePath, fs.F_OK, function(err) {
    if(err){
      done(err,null);
    } else {
      var obj = jsonfile.readFileSync(configFilePath.toString());
      done(null,obj);
    }
  });
}

exports.saveConfig = function(config,done){
  var configFileDir = path.join(mltaDirPath,config.name);
  var configFilePath = configFileDir+'.config';
  jsonfile.writeFile(configFilePath,config,function(err){
    done(err);
  });
}
