from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np

img = imread('tiger-color.png')
# Y=0.2126⋅R+0.7152⋅G+0.0722⋅B
img = img_as_float(img)
r = img[:, :, 0].copy()
g = img[:, :, 1].copy()
b = img[:, :, 2].copy()

y = 0.2126 * r + 0.7152 * g + 0.0722 * b
img = img_as_ubyte(y)
imsave('img_out.png', img)
