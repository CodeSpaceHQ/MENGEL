# Testing Digit Recognition Module

from PIL import Image  # image operations
import os  # directories
import imghdr  # image file recognition
from digit_recognition import digit_recognition
from setup import get_datasets_path
from setup import get_root_path


# Get file count - given a path, returns the number of img files, and the number of non image files
def get_file_count(path):
    img_count = 0
    other_count = 0

    dirs = os.listdir(path)  # store the path.
    imgfiles = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            img_count = img_count + 1
        else:
            other_count = other_count + 1

    return img_count, other_count


# Get score - given a path, performs classification on images in that path,
# and returns the number of correct predictions, incorrect predictions,
# and assigns a score - number of correct/total
def get_score(path, threshold):
    recognizer = digit_recognition(path)
    pred, exp = recognizer.predict_images()
    good = 0
    bad = 0

    for a, b in zip(pred, exp):
        if a == b:
            good = good + 1
        else:
            bad = bad + 1
    score = ((good + 0.0) / (len(pred) + 0.0))
    return score, (score > threshold)


# Get size - given a path and a size, will return the number of images
# of pixel size sizexsize and number that isnt
def get_img_size(path, size):
    size_count = 0
    bad_count = 0

    dirs = os.listdir(path)  # store the path.
    imgfiles = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            img = Image.open(path + item)
            height, width = img.size
            if height == size and width == size:
                size_count = size_count + 1
            else:
                bad_count = bad_count + 1

    return size_count, bad_count


# Performing Testing
path = get_datasets_path()

# img count
img, not_img = get_file_count(path)
print("This classifier only works on image files.")
print("You have " + str(img) + " image files and " + str(not_img) + " non-image files.")

# img sizes
size = 28
good_size, bad_size = get_img_size(path, size)
print("Each image in the path must have same the length and width.")
print("You have " + str(img) + " files of size " + str(size) + " and " + str(bad_size) + " files not of that size.")

# scoring
threshold = 0.80
score, result = get_score(path, threshold)
print("score: " + str(score))
print("Over threshold? : " + str(result))