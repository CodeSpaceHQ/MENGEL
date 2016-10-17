# Tayo Elelu
# Created 10/14/16
# CS 4365 - Software Engr II
# Image Processing Module

# Using Pillow library
# Given a directory, this module will analyze the folder.
# It will go thru all images, resize
# them to 75x75 convert them to grayscale,
# and save the images for later use/output an array of them.

################################################################

#Import needed Pillow libraries
from PIL import Image # image libraries and operations
import os, sys        # directories 
import imghdr         # image file recognition

# Sample Paths
# /mnt/c/Users/Owner/Pictures/SamplePictures/
# /mnt/c/Users/Owner/Documents/SE2CS4365/TestImages/

path = raw_input("Enter the name of the directory you want to manipulate. \n")
dirs = os.listdir(path) # store path
print("Start.")

#list of image types
imgfiles = ['rgb','gif','pbm','pgm','ppm','tiff','rast','xbm','jpeg','jpg','bmp','png','webp','exr']

def resizeFolder():
    for item in dirs:
        print("Converting: " + item)
        if imghdr.what(path+item) in imgfiles:       #if the file has the correct type
            print("Opening image...")
            img = Image.open(path+item).convert('L') #open and convert to greyscale
            a,b = os.path.splitext(path+item)

            newImg = img.resize((75,75), Image.ANTIALIAS) #resize and keep quality
            newImg.save(a + 'edit.jpg', 'JPEG', quality = 90) #save the image with edit appended to it
            print("New image saved: " + item + "\n")

    print("Done!")

resizeFolder()
