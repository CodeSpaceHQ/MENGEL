var rewire = require("rewire");
var expect = require("chai").expect;
var stdin = require('mock-stdin').stdin();

//Logging stuff
var logger = require('tracer').console({
    level: 'warn',
    format: "{{timestamp}} <{{title}}> {{message}} (in {{file}}:{{line}})",
    dateformat: "HH:MM:ss.L"
});

var testConfigObj = {
    name: 'TestName',
    author: 'TestAuthor',
    databaseURL: 'DBURL',
    serviceAccount: 'ServiceAccount'
}

var resultMockObj = {
    author: testConfigObj.author,
    db: testConfigObj.databaseURL,
    sa: testConfigObj.serviceAccount
}

var promptMock = {
    get: function(properties, cb) {
        logger.info("PromptMock");
        cb(null, resultMockObj);
    }
}

var fsMock = {
    accessSync: function(value, status) {
        logger.info('Using FS mock');
        expect(value).to.equal(testConfigObj.serviceAccount);
    }
}

var firebaseManagerMock = {
    connectToFirebase: function(config, cb) {
        logger.info('Using FireebaseManager mock');
        cb(null);
    }
}


var mc = rewire('../mlta-config.js');

mc.__set__({
    fs: fsMock,
    prompt: promptMock,
    fb: firebaseManagerMock
});

describe('config', function() {
    describe('#createNewConfig(name,configFile)', function() {
        it('should create a new config file.', function(done) {
            var configManagerMock = {
                saveConfig: function(config, cb) {
                    logger.info('mock cm.saveConfig')
                    expect(config.name).to.equal(testConfigObj.name)
                    expect(config.author).to.equal(testConfigObj.author)
                    expect(config.databaseURL).to.equal(testConfigObj.databaseURL)
                    expect(config.serviceAccount).to.equal(testConfigObj.serviceAccount)
                    cb(null)
                }
            }
            mc.__set__({
                cm: configManagerMock
            })
            createConfigMethod = mc.__get__('createNewConfig');
            createConfigMethod(testConfigObj.name, new Object());
            stdin.send([
        testConfigObj.name,
        testConfigObj.author,
        testConfigObj.databaseURL,
        testConfigObj.serviceAccount
      ]);
            done();
        })
    })
})
