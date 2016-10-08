var rewire = require("rewire");
var expect = require("chai").expect;
var stdin = require('mock-stdin').stdin();


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
  get: function(properties,cb){
    console.log("PromptMock");
    cb(null,resultMockObj);
  }
}

var fsMock = {
  accessSync: function(value,status){
    console.log("hello");
    expect(value).to.equal(testConfigObj.serviceAccount);
  }
}

var firebaseManagerMock = {
  connectToFirebase: function(config,cb){
    cb(null);
  }
}
var mc = rewire('../mlta-config.js');
mc.__set__({
  fs:'fsMock',
  prompt:'promptMock'
});

describe('config',function(){
  describe('#createNewConfig(name,configFile)',function(){
    it('should create a new config file.',function(done){
      createConfigMethod = mc.__get__('createNewConfig');
      createConfigMethod('configName',new Object());
      stdin.send([
        testConfigObj.author,
        testConfigObj.databaseURL,
        testConfigObj.serviceAccount
      ]);



      done();
    })
  })
})
