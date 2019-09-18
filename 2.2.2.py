from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('img.png')


img = img.max()-img

imsave('out_img.png', img)