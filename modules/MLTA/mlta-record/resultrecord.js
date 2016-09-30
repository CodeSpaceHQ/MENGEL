#!/usr/bin/env node


var program = require('commander');
try{
  var config = require('~/.mlta/config')
} catch(e){
  console.error("Error: Configuration file not found, please run mlta-setup before continuing.")
  process.exit(1);
}

function modelData(val, data) {
  data.push(val);
  return data;
}


function testData(val, data){
  data.push(val);
  return data;
}

//Get arguemnts/options
program
  .version('0.0.1')
  .option('-l, --label <label>' , 'Used to identify specific models for future reference. ')
  .option('-m, --modelType <type>' , 'Type of model used.')
  .option('-d, --modelData <key:value>' , 'Key-value pair of info about the model', modelData , [])
  .option('-D, --testData < key:value>' , 'Key-value pair of info about the test', testData , [])
  .parse(process.argv);

  console.log("Hello user!");
  console.log('Label = %s', program.label)
  console.log("Model= $s", program.modelType)
  console.log('model data = %j' , program.modelData);
  console.log('test data = %j', program.testData);


//Validate arguments/options
