from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('tiger-border.png')

x, y, _ = img.shape
color = img[0, 0]
print(color)
left = sum([(col.all() == color.all())
            for col in [img[:, i]
                        for i in range(y // 2, -1, -1)]])
top = sum([(col.all() == color.all()) for col in [img[i, :] for i in range(x // 2, -1, -1)]])
right = sum([(col.all() == color.all()) for col in [img[:, i] for i in range(y - 1, y // 2, -1)]])
bottom = sum([(col.all() == color.all()) for col in [img[i, :] for i in range(x - 1, x // 2, -1)]])
print(left, top, right, bottom)
