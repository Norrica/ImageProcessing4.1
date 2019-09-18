from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('img.png')

a = img[0,0]
b = [0, 0, 0, 0]
fh = 0
fw = 0
print(img.shape)
for i in img:
    if np.all(i) == np.all(a) and fh == 0:
        b[1] += 1
        continue
    if np.all(i) != np.all(a):
        fh = 1
        continue
    if np.all(i) == np.all(a) and fh == 1:
        fh = 1
        b[3] += 1


for i in img[img.shape[0] // 2]:
    # print(i)
    if np.array_equal(i, a) and fw == 0:
        b[0] += 1
        continue
    if not np.array_equal(i, a):
        fw = 1
        continue
    if np.array_equal(i, a) and fw == 1:
        b[2] += 1

print(*b)
