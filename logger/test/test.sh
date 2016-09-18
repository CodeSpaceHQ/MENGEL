#!/usr/bin/env bash

OUTSRC="./outputs"
SRC="../"

declare -i PASSEDCOUNT=0
declare -i FAILEDCOUNT=0

# Used to print output in nice and neat columns
# Parameters
# - 1: First columns
# - 2: Second Column
function printInCols() {
  printf "%8s | %-20s \n"  $1 $2
}

# Removes the test output file if exists
# Parameters
# - 1: Test Name
function clearPrevTestOutFiles() {
  file=$OUTSRC/$1.out
  if [ -f $file ]; then
    rm $file
  fi
}

# Parameters
# - 1: Test Name
function checkResults() {
  difference=$(diff $OUTSRC/$1.out $OUTSRC/$1.exp)
  if [ "$difference" = "" ]; then
      PASSEDCOUNT=$PASSEDCOUNT+1
      printInCols "PASS" $1
  else
    printInCols "FAILED" $1
    FAILEDCOUNT=$FAILEDCOUNT+1
  fi
}

# Tests the logger using multiple models
function multiModelTest() {
  name=multimodeltest
  clearPrevTestOutFiles $name
  output=$OUTSRC/$name.out
  $SRC/logger.sh -s 90 -l MULTIMODELS -m key11:val11:key12:val12 -m key21:val21:key22:val22 > $output
  checkResults $name
}

# Tests the logger using a single model
function singleModelTest() {
  name=singlemodeltest
  clearPrevTestOutFiles $name
  output=$OUTSRC/$name.out
  $SRC/logger.sh -s 85 -l SINGLEMODEL -m key1:val1:key2:val2:key3:val3 > $output
  checkResults $name
}

# Tests all invalid variations of score
# This time we want to catch errors, STDERR is piped to output file, STDIN is piped to null
function scoreInValidationTest() {
  name=scoreinvalidationtest
  clearPrevTestOutFiles $name
  output=$OUTSRC/$name.out
  $SRC/logger.sh -s 2>> $output 1> /dev/null
  $SRC/logger.sh -s -1 2>> $output 1> /dev/null
  $SRC/logger.sh -s 101 2>> $output 1> /dev/null
  $SRC/logger.sh -s 1.5 2>> $output 1> /dev/null
  checkResults $name

}

# Tests the edge-case valid variations of score
function scoreValidationTest() {
  name=scorevalidationtest
  clearPrevTestOutFiles $name
  output=$OUTSRC/$name.out
  $SRC/logger.sh -s 0 -l "Test1" >> $output
  $SRC/logger.sh -s 51 -l "Test2" >> $output
  $SRC/logger.sh -s 100 -l "Test3" >> $output
  checkResults $name

}

# This test is not only used to generate the output for the README file, but
# also acts as a nice real world example as it has real data.
function readMeExampleTest() {
  name=readmeexampletest
  clearPrevTestOutFiles $name
  output=$OUTSRC/$name.out
  $SRC/logger.sh -s 90 -l Test1 -m trainfile:trainingdata1.csv:testfile:testingdata1.csv:size:3:formula:y~.-3:softmax:true > $output
  checkResults $name

}



printInCols "Results" "Name"
printInCols "=======" "=================="

# Tests
multiModelTest
singleModelTest
scoreValidationTest
scoreInValidationTest
readMeExampleTest


#Making sure the all passed
echo " "
if [ "$FAILEDCOUNT" -eq 0 ]; then
  echo "All tests passed!"
else
  echo "Some tests FAILED!"
fi
