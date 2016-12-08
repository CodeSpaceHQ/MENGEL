from PIL import Image  # image operations
import os     # operations on directories
import imghdr # image file recognition
import numpy  # numpy arrays
import matplotlib #img collection library
matplotlib.use('Agg')

# Sample Paths
# /mnt/c/Users/Owner/Pictures/SamplePictures/
# /mnt/c/Users/Tayo/Documents/SE2CS4365/TestImages/

# list of image types
imgfiles = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']

# Splitting up this module into smaller ones

# Given a filepath and size, resizeFolder will enter the folder
# and edit the files to be square, with lxw as sizexsize
def resize_folder(path, size):
    dirs = os.listdir(path)  # store the path.

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            img = Image.open(path + item)         # open the image
            str_path,ext = os.path.splitext(path + item)  #store the filepath in a string in strpath
            new_img = img.resize((size, size), Image.ANTIALIAS)  # resize and keep quality
            new_img.save(str_path + 'edit.jpg', 'JPEG', quality=90)  # save the image with edit appended to it


# given a directory string, will return an array of numpyarrays of images that have been previously edited
# numpy arrays are used for easy access to the pixel position and pixel hex value information used to classify images
def get_image_array(path):
    img_array = []
    dirs = os.listdir(path)  # store the path.

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            new_img = Image.open(path + item)
            str_path, ext = os.path.splitext(path + item)  #store the filepath in a string in strpath
            if str_path[-4:] == 'edit':                   #if the image has been previously edited
                img_numpy = numpy.array(new_img)  # convert edited images to numpy array
                img_array.append(img_numpy)  # add to array

    return img_array

# given an array of numpyarrays of images, this function will return a csv file representing the info
# each row into the csv represents all info for an image
# each column represents pixel information at a location, there will be (size + 1)
# number of columns in (including an ID column)
# each entry into a column will be a 3-tuple array with the RGB info for the pixel at that location
def get_image_csv(img_array, size)

    for image in img_array
        print("This is image: " + image)
        #write headers?
        #write to ID Column?
        img_row = 0

        row_array = []  #reset the row array to empty

        #nested for loop over the numpy array of image to access pixel info
        for row in range(0,size)
            for col in range(0,size)
                # get info of pixel at that space
                # append to row array
                row_array.append() #append that pixel entry to the row array

        #wrote row array to row of csv file

# given a directory, this will build a string of all the paths to the image,
# and add them to an image collection. to be used to feed into a classifier
# from matplotlib
def build_image_collection(path):
    path_array = []
    dirs = os.listdir(path)  # store the path.

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            str_path, ext = os.path.splitext(path+item)  #store the filepath in a string in strpath
            if str_path[-4:] == 'edit':     # if the image has been previously edited
                path_array.append(str_path + ext)  # add to path array

    image_col = ImageCollection(path_array)
    return image_col