# Low Pass SPatial Domain Filtering  to observe the blurring effect
import cv2
import numpy as np


def average_filter(img, img_name):
    """Average filter"""
    '''Average filter'''
    # Obtain number of rows and columns
    # of the image
    m, n = img.shape

    # Develop Averaging filter(3, 3) mask
    mask = np.full((3, 3), 2)
    mask = mask / 9

    # Convolve the 3X3 mask over the image
    img_new = np.zeros([m, n])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            tmp = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    xx = i + ii
                    yy = j + jj
                    if xx < 0 or xx >= m:
                        continue
                    if yy < 0 or yy >= n:
                        continue
                    tmp += img[xx, yy]
                    # print(ii + 1, jj + 1, mask[ii + 1, jj + 1], sep="  ")

            img_new[i, j] = tmp / 9
            # print(img_new[i, j], img[i, j], sep="   ")

    cv2.imwrite(f'EditedImages/mostly_low_pass_{img_name}.jpg', img_new)
    return img_new
