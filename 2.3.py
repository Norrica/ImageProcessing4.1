from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np

img = imread("00.png")

def align(img, g_coord):
    row_g, col_g = g_coord
    # считаем сдвиги каналов

    # сдвигаем точку на зеленом канале
    # на другие каналы
    return #(row_b, col_b), (row_r, col_r)