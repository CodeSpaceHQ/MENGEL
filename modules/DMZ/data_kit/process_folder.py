from PIL import Image  # image operations
import os     # operations on directories
import imghdr # image file recognition
import numpy  # numpy arrays

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
            strpath,ext = os.path.splitext(path + item)  #store the filepath in a string in strpath
            new_img = img.resize((size, size), Image.ANTIALIAS)  # resize and keep quality
            print(strpath)
            new_img.save(strpath + 'edit.jpg', 'JPEG', quality=90)  # save the image with edit appended to it


# given a directory string, will return the numpyarray of square images that have been previously edited
def get_image_array(path):
    img_array = []
    dirs = os.listdir(path)  # store the path.

    for item in dirs:
        if imghdr.what(path + item) in imgfiles:  # if the file has the correct type
            new_img = Image.open(path + item)
            strpath, ext = os.path.splitext(path + item)  #store the filepath in a string in strpath
            if strpath[-4:] == 'edit':                   #if the image has been previously edited
                img_numpy = numpy.array(new_img)  # convert edited images to numpy array
                img_array.append(img_numpy)  # add to array

    return img_array