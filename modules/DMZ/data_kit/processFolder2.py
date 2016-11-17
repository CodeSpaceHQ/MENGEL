# Import needed libraries
from PIL import Image  # image libraries and operations
import os, sys  # directory libraries
import imghdr  # image file recognition
import numpy  # numpy arrays

# Sample Paths
# /mnt/c/Users/Owner/Pictures/SamplePictures/
# /mnt/c/Users/Tayo/Documents/SE2CS4365/TestImages/

# list of image types
imgfiles = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']


# Splitting up this module into smaller ones

# Given a filepath and size, resizeFolder will enter the folder
# and edit the files to be square, with lxw as sizexsize
def resizeFolder(path, size):
    dirs = os.listdir(path)  # store the path.

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            img = Image.open(path + item)  # .convert('L') #open and convert to greyscale
            a, b = os.path.splitext(path + item)
            newImg = img.resize((size, size), Image.ANTIALIAS)  # resize and keep quality
            newImg.save(a + 'edit.jpg', 'JPEG', quality=90)  # save the image with edit appended to it


# given a directory string, will return the numpyarray of square images with lxw = size x size
def getImageArray(path, size):
    imgArray = []
    width = 0
    height = 0
    dirs = os.listdir(path)  # store the path.

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            newImg = Image.open(path + item)
            width, height = newImg.size
            if width == size and height == size:
                imgNumPy = numpy.array(newImg)  # convert edited images to numpy array
                imgArray.append(imgNumPy)  # add to array

    return imgArray