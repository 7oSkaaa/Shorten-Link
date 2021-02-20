import numpy as np
from scipy import ndimage
from PIL import Image
from matplotlib import pyplot as plt


def sobel_edge_detection(inserted_image, filter):
    new_image_x = ndimage.convolve(inserted_image, filter)
    plt.imshow(new_image_x, cmap='gray')
    plt.title("Vertical Edge")
    plt.show()
    new_image_y = ndimage.convolve(image, np.flip(filter.T, axis=0))
    plt.imshow(new_image_y, cmap='gray')
    plt.title("Vertical Edge")
    plt.show()
    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))
    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    img = Image.fromarray(np.asarray(np.clip(gradient_magnitude, 0, 255), dtype="uint8"), "L")
    img.save("EditedImages/sobel_bike.jpg")


filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

image = Image.open("Images/Bikesgray.jpg")
sobel_edge_detection(image, filter)
