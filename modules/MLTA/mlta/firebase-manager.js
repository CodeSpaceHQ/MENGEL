#!/usr/bin/env node

var firebase = require("firebase"); //For Firebase stuff..duh..

//Paths in the Firebase database
var fbMainDir = '/mlta';
var fbResultDir = fbMainDir + '/results/'

//Logging stuff
var tracer = require('tracer');
tracer.setLevel(5) //'log':0, 'trace':1, 'debug':2, 'info':3, 'warn':4, 'error':5
var logger = tracer.console({
    format: "{{timestamp}} <{{title}}> {{message}} (in {{file}}:{{line}})",
    dateformat: "HH:MM:ss.L"
});


var exports = module.exports = {};

/*
  Handles initializing firebase and checking authentication.
*/
exports.connectToFirebase = function(mltaConfig, done) {
    var fbConfig = {
        serviceAccount: mltaConfig.serviceAccount,
        databaseURL: mltaConfig.databaseURL,
        authDomain: mltaConfig.authDomain
    };

    firebase.initializeApp(fbConfig);

    var db = firebase.database();

    //If we don't have a connection in a few seconds, whether its due to incorrect credintials, or network error, we cannot continue.
    var connFailTimeout = setTimeout(function() {
        logger.error('Connection timed out connecting to Firebase');
        var error = new Error('Failed to connect to Firebase.');
        done(error);
    }, 10000);

    //Called if we have an established, authorized connection to the Firebase database
    function ready() {
        clearTimeout(connFailTimeout); //We've connected to lets go ahead and tell the connFailTimeout dude up there ^ that he can leave his post.
        done(null);
    }

    //The way the mock firebase-server currently works, the database is offline so we have to do it this way
    if(mltaConfig.name === "MLTA-Test") {
        ready();
    }
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
            logger.info('Connected to Firebase.');
            db.ref('.info/connected').off('value', connFunc);
            ready();
        }
    });
}


/*
  Saves the result object to the Firebase database.
  The object is saved with a UID that is generated and returned here.
  done(error,UID)
*/
exports.saveResult = function(result, done) {
    logger.info('Saving result to Firebase');
    logger.debug('Result: %j',result);

    // Get a key for a new Post.
    var resultKey = firebase.database().ref().child(fbResultDir).push().key;

    var updates = {};
    updates[fbResultDir + resultKey] = result;

    //This is more a less a hack till the local firebase-server issues get figured out.
    if(result.isTest) {
        done(null, resultKey);
        return;
    }

    var fbp = firebase.database().ref().update(updates);
    fbp.then(
        function(val) {
            logger.info('Saved result to Firebase');
            logger.debug('Generated result UID: %s',resultKey);
            done(null, resultKey);
        }
    ).catch(
        function(reason) {
            logger.error('Failed to update Firebase');
            logger.debug('Rason: %j',reason);
            done(reason);
        }
    )
}
