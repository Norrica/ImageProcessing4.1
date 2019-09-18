from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('img.png')

red = img[:,:,0].copy()
green = img[:,:,1].copy()
blue = img[:,:,2].copy()

img[:,:,0] = blue
img[:,:,1] = red
img[:,:,2] = green

imsave('img_out.png', img)