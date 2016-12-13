# Overview
This README.md details the module for digit recognition in digit_recognition.py

## Classes and Functions
- class digit_recognition: contains both the init and predict images function. Contains global variables for testing and training data.
- def __init__(self, path): Initializes a digit_recognition object, that contains testing & training data, based on the given path.
- def predict_images(self): performs svm classification on the training data, and predicts with testing data. Returns two lists - one of predictions, and one of expected values.