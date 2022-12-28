import cv2


def histo_eq(img, img_name):
    """Histogram equalization"""
    res = cv2.equalizeHist(img)
    cv2.imwrite(f'EditedImages/histo_equalization_{img_name}.png', res)
    return res
