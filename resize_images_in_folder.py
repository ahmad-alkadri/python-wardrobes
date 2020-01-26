#### PYTHON CODE: RESIZE IMAGES IN A FOLDER ####
#### Dependances: PIL, os, sys, glob

from PIL import Image
import os, sys, glob

# Define the desired final width
finalwidth = 1200 	 # in pixels

# Define the type of images that you want to resize
types = ('*.png','*.jpg','*.jpeg') 

# Get current path
path = os.getcwd()

# Get list of images in current path
items = []
for files in types:
    items.extend(glob.glob(files))

# Resize all images
for item in items:
    if os.path.isfile(path+'/'+item):
        img = Image.open(path+'/'+item)
        wpercent = (finalwidth/float(img.size[0]))
        widthimg = img.size[0]
        heightimg = img.size[1]
        if finalwidth < widthimg:
        	hsize = int((float(img.size[1])*float(wpercent)))
        	imgResize = img.resize((finalwidth,hsize), Image.ANTIALIAS)
        	imgResize.save(path+'/'+ item, quality=90)
