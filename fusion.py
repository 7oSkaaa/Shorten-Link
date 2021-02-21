import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def fangcha(img):
    row = img.shape[0]
    col = img.shape[1]
    varImg = np.zeros([row, col])
    for i in range(row):  # seeking the variance range
        for j in range(col):
            if i - 5 > 0:
                up = i - 5
            else:
                up = 0
            if i + 5 < row:
                down = i + 5
            else:
                down = row
            if j - 5 > 0:
                left = j - 5
            else:
                left = 0
            if j + 5 < col:
                right = j + 5
            else:
                right = col
            window = img[up:down, left:right]
            Mean, var = cv.meanStdDev(window)  # Call the OpenCV function to find the mean and variance
            varImg[i, j] = var
    return varImg


def qiuquan(img1, img2):
    row = img1.shape[0]
    col = img1.shape[1]
    array1 = fangcha(img1)  # call the variance function
    array2 = fangcha(img2)
    for i in range(row):  # Author
        for j in range(col):
            weight1 = array1[i, j] / (array1[i, j] + array2[i, j])
            weight2 = array2[i, j] / (array1[i, j] + array2[i, j])
            array1[i, j] = weight1
            array2[i, j] = weight2
    return array1, array2


def ronghe(img1, img2):
    cc = img1.copy()
    b, g, r = cv.split(img1)  # sub-channel processing
    b1, g1, r1 = cv.split(img2)
    weight1, weight2 = qiuquan(b, b1)  # call weighting function
    weight11, weight22 = qiuquan(g, g1)
    weight111, weight222 = qiuquan(r, r1)
    new_img = img1 * 1
    row = new_img.shape[0]
    col = new_img.shape[1]
    b2, g2, r2 = cv.split(cc)
    for i in range(row):  # image fusion
        for j in range(col):
            b2[i, j] = (weight1[i, j] * b[i, j] + weight2[i, j] * b1[i, j]).astype(int)
            g2[i, j] = (weight11[i, j] * g[i, j] + weight22[i, j] * g1[i, j]).astype(int)
            r2[i, j] = (weight111[i, j] * r[i, j] + weight222[i, j] * r1[i, j]).astype(int)
        new_img = cv.merge([b2, g2, r2])  # Channel merge
    return new_img


img1 = cv.imread("Images/clearleft.jpeg")
img2 = cv.imread("Images/clearright.jpeg")
img3 = ronghe(img1, img2)
cv.imwrite("EditedImages/fusioned_beach_Image.jpeg", img3)
