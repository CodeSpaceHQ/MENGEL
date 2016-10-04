#!/usr/bin/env node
var assert = require('assert');
var FirebaseServer = require('firebase-server');
var firebase = require("firebase"); //For Firebase stuff..duh..
var expect    = require("chai").expect;

var fm = require('../firebase-manager.js');


var fs = new FirebaseServer(5000, 'localhost.firebaseio.test', {
  info: {
    alive: true
  }
});

var config = {
  name: "MLTA-Test",
  author: "MLTA-Test-Author",
  authDomain:  "localhost.firebaseio.test:5000",
  databaseURL: "localhost.firebaseio.test:5000"
};

describe('firebase-manager',function(){
  this.timeout(10000);
  after(function(){
    fs.close(); //Closes the firebase-server when done.
  });


  describe('#connectToFirebase(mltaConfig,cb)',function(){
    it('should connect to the firebase server', function(done){
      fm.connectToFirebase(config,function(err){
        expect(err).to.be.null;
        done(err);
      });
    });
  });
});
