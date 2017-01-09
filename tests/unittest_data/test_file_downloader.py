import urllib

testfile = urllib.URLopener()
testfile.retrieve("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", "tests/unittest_data/winequality-red.csv")
