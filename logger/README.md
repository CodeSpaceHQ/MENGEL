# Logger
## Purpose
To handle automatically logging of all tests.
By tests we mean, testing an actual algorithm (as opposed to tests that test the framework itself).


## Usage Instructions
```
usage: ./logger.sh -s score [-h] [-m model] [-l label] [-o location]
  -s score      Score from results, must be an integer in [0,100]
  -h            Displays these usage instructions
  -c            Auto commit file (Make sure your git global config is setup properly)
  -m model      Pass in a key value pair for the model, must be in format key1:value1:key2:value2:
  -l label      Label that can be used to identify this test later
  -o location   Location for output files (defaults to ./output/)
```

### Example usage
Let's say we are wanting to use a nueral net in an R program and we have chosen to use the `nnet` package.
We might create the 'nnet' model with code similiar to this:
```R
library(nnet)
data.train<-read.csv("./trainingdata1.csv")
data.test<-read.csv("./testingdata1.csv")
labels<-class.ind(factor(data.train[,3]))
model<-nnet(
    train.data[,-3],
    labels,
    size=3,
    softmax=TRUE
  )
result<-predict(model,data.test[,-3],type="class")
```
In this example, we are trying to predict the values of column 3 in the data using all other columns.
After we have created this model, and tested its prediction, we will want to record enough about this model and test in order for us to recreated this as closely as possible later.

Things we might want to save for future reference could be:
- Testing/training file names
- Number of units in the hidden layer (size).
- Formula used for input (in this case we just passed a data frame without column 3)
- The percentage of correct predictions from the `result` from the `predict(...)` function call.
- Whether or not we used softmax error for classification

Let's assume our score was 90%.
For ease of use, let's lavel this test as "Test1". While the label is not needed, it can be used to easily distinquish in a human-readable form various tests from each other.

We can record our model and results like so:
```
./logger.sh -s 90 -l Test1 -m trainfile:trainingdata1.csv:testfile:testingdata1.csv:size:3:formula:y~.-3:softmax:true
```
And in which case our expected output would look like:
```
{  
   "label":"Test1",
   "score":"90",
   "model0":{  
      "trainfile":"trainingdata1.csv",
      "testfile":"testingdata1.csv",
      "size":"3",
      "formula":"y~.-3",
      "softmax":"true"
   }
}
```
