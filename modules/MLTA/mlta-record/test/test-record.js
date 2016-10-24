var rewire = require("rewire");
var expect = require("chai").expect;
var stdin = require('mock-stdin').stdin();

//Logging stuff
var tracer = require('tracer');
tracer.setLevel(5) //'log':0, 'trace':1, 'debug':2, 'info':3, 'warn':4, 'error':5
var logger = tracer.console({
    format: "{{timestamp}} <{{title}}> {{message}} (in {{file}}:{{line}})",
    dateformat: "HH:MM:ss.L"
});


//Mocking stuff
var programOptionsMockObj = {
    modelData: {
        'mockModelDataKey1': 'mockModelDataVal1',
        'mockModelDataKey2': 'mockModelDataVal2'
    },
    testData: {
        'mockTestDataKey1': 'mockTestDataVal1',
        'mockTestDataKey2': 'mockTestDataVal2'
    }
}

var configObjMock = {
    author: 'TestAuthor'
}

var fsMock = {
    access: function(configFile, status, cb) {
        logger.info('Mock: fs.access');
        expect(configFile).to.be.an('string');
        cb(null);
    }
}
var firebaseManagerMock = {
    connectToFirebase: function(config, cb) {
        logger.info('Mock: fb#connectToFirebase')
        expect(config.author).to.equal(configObjMock.author);
        cb(null);
    },
    saveResult: function(result, cb) {
        logger.info('Mock: fb#saveResult');
        expect(result.label).to.equal(programOptionsMockObj.label);
        expect(result.author).to.equal(configObjMock.author);
        expect(result.modelType).to.equal(programOptionsMockObj.modelType);
        expect(result.modelData).to.equal(programOptionsMockObj.modelData);
        expect(result.testData).to.equal(programOptionsMockObj.testData);
        cb(null);
    }
}

var jsonFileMock = {
    readFileSync: function(configFileName) {
        expect(configFileName).to.be.an('string');
        return configObjMock;
    }
}

var recordModule = rewire('../mlta-record.js');
recordModule.__set__({
    fs: fsMock,
    fb: firebaseManagerMock,
    jsonfile: jsonFileMock
});


//Helper method stuff
function expectError(err,message){
  expect(err).to.be.an('error');
  expect(err.message).to.equal(message)
}


/**
  TEST METHODS GO BELOW HERE

/**
Let false validation tests run first(in order that mlta-record checks the data), then they each add the data they were
checking against to the mock obj.
*/

describe('record', function() {
    describe('#validateOptions(program, done)', function() {
        validateOptionsMethod = recordModule.__get__('validateOptions');
        it('should return an error when the project name is missing', function(done) {
            validateOptionsMethod(programOptionsMockObj, function(err, options) {
              expectError(err,'Project name must be specified.')
                programOptionsMockObj.project = 'MockProjectName';
                done();
            })
        })
        it('should return an error when the model type is missing', function(done) {
            validateOptionsMethod(programOptionsMockObj, function(err, options) {
              expectError(err,'Model type must be specified.')
                programOptionsMockObj.modelType = 'TestModelType';
                done();
            })
        })
        it('should return an options object with an empty string for label if no label is passed in upon valid input', function(done) {
            validateOptionsMethod(programOptionsMockObj, function(err, options) {
                expect(err).to.be.null;
                expect(options.label).to.equal('');
                programOptionsMockObj.label = 'TestLabel';
                done();
            })
        })
        it('should return an options object with validated data upon valid input', function(done) {
            validateOptionsMethod(programOptionsMockObj, function(err, options) {
                expect(err).to.be.null;
                expect(options.project).to.equal(programOptionsMockObj.project);
                expect(options.label).to.equal(programOptionsMockObj.label);
                expect(options.modelType).to.equal(programOptionsMockObj.modelType);
                expect(options.modelData).to.equal(programOptionsMockObj.modelData);
                expect(options.testData).to.equal(programOptionsMockObj.testData);
                done();
            })
        })
    })

    describe('#saveRecordToFB(options)', function() {
        saveRecordToFBMethod = recordModule.__get__('saveRecordToFB');

        it('should create a result record using config and passed in options then save created record to firebase.', function(done) {
            saveRecordToFBMethod(programOptionsMockObj, function(err) {
                expect(err).to.be.null;
                done();
            })
        })

    })
})
