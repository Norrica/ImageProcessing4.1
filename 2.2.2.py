from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('tiger-color.png')


img = img.max()-img

imsave('img.png', img)