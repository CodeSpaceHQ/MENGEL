import urllib

testfile = urllib.URLopener()
testfile.retrieve("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", "winequality-red.csv")
