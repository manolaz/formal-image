import glob
import pathlib    
from PIL import Image
mainfolder = input("Input folder: ") 

p = pathlib.Path("{}/".format(mainfolder))

def compress(img_file):
    print(img_file)
    basewidth = 1920
    img = Image.open(img_file)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(img_file)

for img_file in p.rglob("*.png"):
    compress(img_file)

for img_file in p.rglob("*.jpg"):
    compress(img_file)

for img_file in p.rglob("*.jpeg"):
    compress(img_file)