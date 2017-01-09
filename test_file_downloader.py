import urllib

testfile = urllib.URLopener()
testfile.retrieve("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", "datasets/winequality-red.csv")
testfile.retrieve("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", "datasets/winequality-white.csv")
