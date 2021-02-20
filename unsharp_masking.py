import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import median_filter
import numpy as np


def un_sharp(image, sigma, strength):
    # Median filtering
    image_mf = median_filter(image, sigma)
    # Calculate the Laplacian
    lap = cv2.Laplacian(image_mf, cv2.CV_64F)
    # Calculate the sharpened image
    sharp = image - strength * lap
    sharp[sharp > 255] = 255
    sharp[sharp < 0] = 0
    return sharp


original_image = plt.imread('Images/bird.jpg')
sharp1 = np.zeros_like(original_image)

# In order to sharp RGB images
for i in range(3):
    sharp1[:, :, i] = un_sharp(original_image[:, :, i], 5, 0.8)

plt.imshow(sharp1)
plt.show()
