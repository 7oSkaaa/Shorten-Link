import numpy as np
from scipy import ndimage
from PIL import Image

# ALL IMAGES INSERTED INTO ROBERT CROSS SHOULD BE GRAY SCALE . (THE BIRD IMAGE WON'T WORK FOR EXAMPLE)
roberts_cross_v = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, -1]])

roberts_cross_h = np.array([[0, 0, 0],
                            [0, 0, 1],
                            [0, -1, 0]])


def load_image(infile_name):
    img = Image.open(infile_name)
    img.load()
    # note signed integer
    return np.asarray(img, dtype="int32")


def save_image(data, outfile_name):
    img = Image.fromarray(np.asarray(np.clip(data, 0, 255), dtype="uint8"), "L")
    img.save(outfile_name)


def roberts_cross(infile_name, outfile_name):
    image = load_image(infile_name)
    vertical = ndimage.convolve(image, roberts_cross_v)
    horizontal = ndimage.convolve(image, roberts_cross_h)
    output_image = np.sqrt(np.square(horizontal) + np.square(vertical))
    save_image(output_image, outfile_name)


roberts_cross('Images/Bikesgray.jpg', 'EditedImages/edited_bikesgray.jpg')
