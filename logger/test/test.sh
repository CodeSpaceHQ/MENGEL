#!/usr/bin/env bash

EXPSRC="./expectedOutputs"
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

# Compares the output file with a file that holds the expected result.
# If the test passes, the test output file is removed.
# Parameters
# - 1: Test Name
# - 2: Logger output
function checkResults() {
  difference=$(diff $2 $EXPSRC/$1.exp)
  if [ "$difference" = "" ]; then
      PASSEDCOUNT=$PASSEDCOUNT+1
      printInCols "PASS" $1
      rm $2
  else
    printInCols "FAILED" $1
    FAILEDCOUNT=$FAILEDCOUNT+1
  fi
}

# Tests the logger using multiple models
function multiModelTest() {
  name=multimodeltest
  output=$($SRC/logger.sh -s 90 -l MULTIMODELS -m key11:val11:key12:val12 -m key21:val21:key22:val22 -o $OUTSRC)
  checkResults $name $output
}

# Tests the logger using a single model
function singleModelTest() {
  name=singlemodeltest
  output=$($SRC/logger.sh -s 85 -l SINGLEMODEL -m key1:val1:key2:val2:key3:val3 -o $OUTSRC)
  checkResults $name $output
}

# Tests all invalid variations of score
# This time we want to catch errors, STDERR is piped to output file, STDIN is piped to null
function scoreInValidationTest() {
  name=scoreinvalidationtest
  clearPrevTestOutFiles $name
  outputsrc=$OUTSRC/$name.out

  output1=$($SRC/logger.sh -s 2>&1 > /dev/null) # 2>> $output 1> /dev/null
  echo $output1 >> $outputsrc
  output2=$($SRC/logger.sh -s -1 2>&1 > /dev/null) # 2>> $output 1> /dev/null
  echo $output2 >> $outputsrc
  output3=$($SRC/logger.sh -s 101 2>&1 > /dev/null) # 2>> $output 1> /dev/null
  echo $output3 >> $outputsrc
  output4=$($SRC/logger.sh -s 1.5 2>&1 > /dev/null) # 2>> $output 1> /dev/nul
  echo $output4 >> $outputsrc
  checkResults $name $outputsrc

}

# Tests the edge-case valid variations of score
function scoreValidationTest() {
  name=scorevalidationtest
  clearPrevTestOutFiles $name
  outputsrc=$OUTSRC/$name.out


  output1=$($SRC/logger.sh -s 0 -l "Test1" -o $OUTSRC)
  cat $output1 >> $outputsrc
  rm $output1
  output2=$($SRC/logger.sh -s 51 -l "Test2" -o $OUTSRC)
  cat $output2 >> $outputsrc
  rm $output2
  output3=$($SRC/logger.sh -s 100 -l "Test3" -o $OUTSRC)
  cat $output3 >> $outputsrc
  rm $output3

  checkResults $name $outputsrc

}

# This test is not only used to generate the output for the README file, but
# also acts as a nice real world example as it has real data.
function readMeExampleTest() {
  name=readmeexampletest

  output=$($SRC/logger.sh -s 90 -l Test1 -m trainfile:trainingdata1.csv:testfile:testingdata1.csv:size:3:formula:y~.-3:softmax:true -o $OUTSRC)
  checkResults $name $output

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
