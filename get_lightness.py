import numpy as np
from PIL import Image


def get_lightness_func(imgpath):
    img = Image.open(imgpath)
    img_color = np.array(img)

    img_y = np.shape(img_color)[0]
    img_x = np.shape(img_color)[1]

    lightness_array = np.zeros((img_x * img_y))
    i = 0
    for row in img_color:
        for pixel in row:
            lightness = sum(pixel) / 3
            lightness_array[i] = lightness
            i += 1

    return lightness_array
