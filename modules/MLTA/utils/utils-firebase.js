#!/usr/bin/env node
var firebase = require("firebase"); //For Firebase stuff..duh..

var exports = module.exports = {};

//Handles initializing firebase and checking authentication.
exports.connectToFirebase = function(mltaConfig,configFilePath,cb){
  var fbConfig = {
    serviceAccount: mltaConfig.serviceAccount,
    databaseURL: mltaConfig.databaseURL
  };
  firebase.initializeApp(fbConfig);
   var db = firebase.database();

   //If we don't have a connection in a few seconds, whether its due to incorrect credintials, or network error, we cannot continue.
   var connFailTimeout = setTimeout(function() {
     var error = new Error('Failed to connect to Firebase.');
     cb(errow);
   }, 10000);

   //Called if we have an established, authorized connection to the Firebase database
  function ready() {
    clearTimeout(connFailTimeout); //We've connected to lets go ahead and tell the connFailTimeout dude up there ^ that he can leave his post.
    cb(null);


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
