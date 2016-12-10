#!/usr/bin/env node

var path = require('path'); //Handles path naming
var fs = require('fs') //fs = filesystem, used for creating/opening/writing files
var jsonfile = require('jsonfile') //Config files are in JSON format

//Logging stuff
var tracer = require('tracer');
tracer.setLevel(5) //'log':0, 'trace':1, 'debug':2, 'info':3, 'warn':4, 'error':5
var logger = tracer.console({
    format: "{{timestamp}} <{{title}}> {{message}} (in {{file}}:{{line}})",
    dateformat: "HH:MM:ss.L"
});


var mltaDirPath = path.join(process.env.HOME, '.mlta'); //This var basically holds this: ~/.mlta

var exports = module.exports = {};

//Returns error if config does not exists

/*
  Config files are created and stored as [Project-Name].config
  Returns config objc for given Project-Name.
  Returns error if config doesn't exists.
  - This can happen due to permission issues or because the project config doesn't exist
*/
exports.getConfigIfExists = function(name, done) {
    logger.info('Looking for config for project %s', name);
    var configFileDir = path.join(mltaDirPath, name);
    var configFilePath = configFileDir + '.config';
    fs.access(configFilePath, fs.F_OK, function(err) {
        if(err) {
          logger.warn('Error loading config for %s, maybe it doesn\'t exist yet?',name);
            done(err, null);
        } else {
            var obj = jsonfile.readFileSync(configFilePath.toString());
            done(null, obj);
        }
    });
}

/*
  Writes config as a JSON objc to file PROJECT_NAME].config
  Will overwrite any existing file by that name.
*/
exports.saveConfig = function(config, done) {
    logger.info('Saving config');
    logger.debug('Config: %j', config);
    var configFileDir = path.join(mltaDirPath, config.name);
    var configFilePath = configFileDir + '.config';
    jsonfile.writeFile(configFilePath, config, {spaces: 2},function(err) {
        done(err);
    });
}
