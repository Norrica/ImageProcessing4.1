from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('tiger-border.png')

a = img[0,0]
b = [0, 0, 0, 0]


for i in img:
    if np.all(i) == np.all(a):
        b[1] += 1
    else:
        break
for i in reversed(img):
    if np.all(i) == np.all(a):
        b[3] += 1
    else:
        break

for i in img[img.shape[0] // 2]:
    if np.array_equal(i, a):
        b[0] += 1
    else:
        break

for i in reversed(img[img.shape[0] // 2]):
    if np.array_equal(i, a):
        b[2] += 1
    else:
        break

print(*b)
