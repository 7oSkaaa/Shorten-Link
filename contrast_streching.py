import cv2
import numpy as np


def contrast_stretching(img):
    """Contrast stretching"""
    # normalize float versions
    norm_img1 = cv2.normalize(img, None, alpha=2, beta=4, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # scale to uint8
    norm_img1 = (255 * norm_img1).astype(np.uint8)
    norm_img2 = np.clip(norm_img2, 0, 1)
    norm_img2 = (255 * norm_img2).astype(np.uint8)

    # write normalized output images
    cv2.imwrite("EditedImages/contrast1.jpg", norm_img1)
    cv2.imwrite("EditedImages/contrast2.jpg", norm_img2)
    return norm_img2
