#Digit Recognition Module

# Standard scientific Python imports
import matplotlib
matplotlib.use('Agg')   #Force matplotlib to not use any Xwindows backend (causes errors)
from sklearn import svm # Import svm classifier
import skimage.io       # reading images
import os     # directories
import imghdr # image file recognition
import numpy  # numpy arrays

#the init function will enter the paths given, which contain the images needed for testing and training
#init will put them into the format needed for the classifier, and return a tuple of two lists
#corresponding to the testing and training data
#returns a zipped list, where element[0] is the testing data and [1] is the training data
#unzip to get both the images and the predictions
def init(path):

    img_array = []
    target_array = []
    dirs = os.listdir(path)  # store the path.
    imgfiles = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']
    path_length = len(path)

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:    # if the file has the correct type
            str_path, ext = os.path.splitext(path + item)  # store the filepath in a string in strpath
            img_array.append(skimage.io.imread(str_path + ext)) #add image to img_array
            target_str = str_path[path_length:]  # build the target array to correspond with image collection
            target_str = target_str[:7]
            target_int = int(target_str[-1:]) #get the number that the img represents from the filename
            target_array.append(target_int) #append to target_array

    #Build the matrix of rows x features
    n_samples = len(img_array)
    features = 28 * 28  # size of image
    row_array = []
    matrix = []

    for member in (img_array):  # build the matrix
        row_array = numpy.reshape(member, (features))
        matrix.append(row_array)

    #randomize the data
    a = tuple(matrix)
    b = tuple(target_array)
    zip_list = list(zip(a,b))      # tie each entry in the matrix to its prediction value
    numpy.random.shuffle(zip_list) # randomize

    train_int = int(0.7 * n_samples)  #amt of data for training
    test_int = n_samples - train_int  #amt of data for testing

    train_data = zip_list[:test_int] #70% of the data stored in train_data
    test_data = zip_list[-test_int:] #30% of the data stored in test_data

    #return a tuple of zipped lists
    return train_data, test_data



# Given a data in the form of a tuple of two zipped lists (each image is paired with its classification)
# and each list corresponds to testing & training data,
# This function creates a SVM classifier, fits the data using the training data
# and returns a tuple of two lists - one list is the prediction, one is the actual value.
def predict_images(class_data):
    train_data, test_data = class_data[0], class_data[1]   # get testing & training data
    matrix_train_tup, digits_train_tup = zip(*train_data)  # unzip the randomized training list
    matrix_train = list(matrix_train_tup)
    digits_train = list(digits_train_tup)

    # Create a classifier: a support vector classifier
    classifier = svm.SVC(C=1.0, tol=1e-10, cache_size=600, kernel='rbf', gamma=0.00000001)

    # Classify the Training Data with the fit() function
    classifier.fit(matrix_train, digits_train)

    # Get the prediction list using the testing data
    matrix_test_tup, digits_test_tup = zip(*test_data)  # unzip the randomized testing list
    matrix_test = list(matrix_test_tup)
    digits_test = list(digits_test_tup)

    #get expected and predicted values in list form
    expected = digits_test
    predicted = list(classifier.predict(matrix_test))

    #return a tuple of two lists
    return predicted, expected

#Testing
path = "/mnt/c/Users/Tayo/Documents/SE2CS4365/HandWrittenChar/eggChar/mnist_jpgfiles/trainsmall/"
pred, exp = predict_images(init(path))

print("Last 20 predictions: ")
print(pred[-20:])
print("Last 20 expected values:")
print(exp[-20:])