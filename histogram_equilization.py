import cv2
import numpy as np


def histo_eq(img):
    """Histogram equalization"""
    res = cv2.equalizeHist(img)
    #res = np.hstack((img, equ))  # stacking images side-by-side
    cv2.imwrite('EditedImages/histo_eq.png', res)
    return res
