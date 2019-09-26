from __future__ import print_function
import PIL
from PIL import Image
import glob
import os, sys
from utils import find_files_recursive


def resize(path, baseheight=900):
    try:
        img = Image.open(path)
        size = img.size
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        if baseheight != img.size[1]:
            img = img.resize((wsize, baseheight), resample=Image.LANCZOS)
            img.save(path)
            print("Resized: ", size , " -> ",(wsize, baseheight) , path)
    except IOError:
        print(" - ")



if __name__ == '__main__':
    root_dir = os.getcwd()
    for filename in find_files_recursive(root_dir):
        print(filename)
        resize(filename)