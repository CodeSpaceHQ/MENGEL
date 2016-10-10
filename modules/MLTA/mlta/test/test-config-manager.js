#!/usr/bin/env node

var assert = require('assert');
var cm = require('../config-manager.js');
var expect = require("chai").expect;

var config = {
    name: "TestConfigName",
    author: "authorName",
    databaseUrl: "wwww.databaseurl.com",
    serviceAccount: "locationServiceAccount"
}

describe('config-manager', function() {

    describe('#saveConfig(config,done)', function() {
        it('should write the config to a JSON file', function(done) {
            cm.saveConfig(config, function(err) {
                expect(err).to.be.null;
                done(err);
            });
        });
    });

    describe('#getConfigIfExists(name,done)', function() {
        it('should return an error if config file does not exist', function(done) {
            cm.getConfigIfExists("someFakeConfigName", function(err, config) {
                expect(err).to.be.an('error');
                done();
            });
        });

        it('should return a config object if config file does exist', function(done) {
            cm.getConfigIfExists(config.name, function(err, newConfig) {
                expect(config.name).to.equal(newConfig.name);
                expect(config.author).to.equal(newConfig.author);
                expect(config.databaseURL).to.equal(newConfig.databaseURL);
                expect(config.serviceAccount).to.equal(newConfig.serviceAccount);
                done(err);
            });
        });
    });
})
