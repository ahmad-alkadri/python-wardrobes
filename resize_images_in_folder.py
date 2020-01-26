#### PYTHON CODE: RESIZE IMAGES IN A FOLDER ####
#### Dependances: PIL, os, sys, glob

#### DESCRIPTION
#### Like its name implies, this code is useful for resizing many images
#### in a particular folder all at once. The idea is having a code that 
#### you can launch once and resize all the images based on their width
#### and keeping their aspect ratio. Be careful: the saved image will have
#### the same file name as its original one. Essentially, it will replace
#### the original file with the resized one.

#### HOW TO USE
#### This code depends on four Python modules: PIL, os, sys, and glob.
#### All of them are installable through conda or pip (and normally, 
#### if you install your Python through distributions such as Anaconda,
#### those packages are already installed. If not, please install them first.
#### If those packages are installed already, just put this code in the same 
#### folder where your original images are residing, then launch it.

#### CUSTOMIZATION
#### 1) By default, the image types that will be converted are PNG, JPG, and JPEG
####    (see line 35). You can of course add more image extensions such as TIF.
#### 2) By default, the final width is 1200 (see line 32). You can always
####    modify it.
#### 3) All images with width size already smaller than finalwidth will not
####    be modified.

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
