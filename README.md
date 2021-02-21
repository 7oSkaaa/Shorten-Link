# IPApps

IP apps( Image processing applications) is a reposotiry which includes all the python & Shell code used to obtain :
- All edge detection levels
- Image restoration
- Compression
- & others

## Roberts cross operator

The Roberts cross operator is used in image processing and computer vision for edge detection. It was one of the first edge detectors and was initially proposed by Lawrence Roberts in 1963.As a differential operator, the idea behind the Roberts cross operator is to approximate the gradient of
an image through discrete differentiation which is achieved by computing the sum of the squares of the differences between diagonally adjacent pixels.

According to Roberts, an edge detector should have the following properties: the produced edges should be well-defined, the background should contribute as little noise as possible, and the intensity of edges should correspond as close as possible to what a human would perceive.

[Robert cross operator Implementation](https://github.com/MeitanteiAshour/IPApps/blob/master/robertopt.py)

## Prewit operator 

The Prewitt operator is used in image processing, particularly within edge detection algorithms. Technically, it is a discrete differentiation operator, computing an approximation of the gradient of the image intensity function. At each point in the image, the result of the Prewitt operator is either the corresponding gradient vector or the norm of this vector. The Prewitt operator is based on convolving the image with a small, separable, and integer valued filter in horizontal and vertical directions and is therefore relatively inexpensive in terms of computations like Sobeloperatos. On the other hand, the gradient approximation which it produces is relatively crude, in particular for high frequency variations in the image. The Prewitt operator was developed by Judith M. S. Prewitt.

[Prewit operator Implementation](https://github.com/MeitanteiAshour/IPApps/blob/master/prewit_opt.py)

## Sobel operator

The Sobel operator, sometimes called the Sobel–Feldman operator or Sobel filter, is used in image processing and computer vision, particularly within edge detection algorithms where it creates an image emphasising edges. It is named after Irwin Sobel and Gary Feldman, colleagues at the Stanford Artificial Intelligence Laboratory (SAIL). Sobel and Feldman presented the idea of an "Isotropic 3x3 Image Gradient Operator" at a talk at SAIL in 1968.Technically, it is a discrete differentiation operator, computing an approximation of the gradient of the image intensity function. At each point in the image, the result of the Sobel–Feldman operator is either the corresponding gradient vector or the norm of this vector. The Sobel–Feldman operator is based on convolving the image with a small, separable, and integer-valued filter in the horizontal and vertical directions and is therefore relatively inexpensive in terms of computations. On the other hand, the gradient approximation that it produces is relatively crude, in particular for high-frequency variations in the image.

[Sobel operator Implementation](https://github.com/MeitanteiAshour/IPApps/blob/master/sobel_op.py)

## Kirsch operator

The Kirsch operator or Kirsch compass kernel is a non-linear edge detector that finds the maximum edge strength in a few predetermined directions. It is named after the computer scientist Russell Kirsch.
The operator takes a single kernel mask and rotates it in 45 degree increments through all 8 compass directions: N, NW, W, SW, S, SE, E, and NE. The edge magnitude of the Kirsch operator is calculated as the maximum magnitude across all directions:

[Kirsch operator Implementation](https://en.wikipedia.org/wiki/Kirsch_operator)

## Spatial filtering

A spatial filter is an optical device which uses the principles of Fourier optics to alter the structure of a beam of light or other electromagnetic radiation, typically coherent laser light. Spatial filtering is commonly used to "clean up" the output of lasers, removing aberrations in the beam due to imperfect, dirty, or damaged optics, or due to variations in the laser gain medium itself. This filtering can be applied to transmit a pure transverse mode from a multimode laser while blocking other modes emitted from the optical resonator.The term "filtering" indicates that the desirable structural features of the original source pass through the filter, while the undesirable features are blocked. Apparatus which follows the filter effectively sees a higher-quality but lower-powered image of the source, instead of the actual source directly. An example of the use of spatial filter can be seen in advanced setup of micro-Raman spectroscopy.

Examples : 

## Median filtering

The median filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Such noise reduction is a typical pre-processing step to improve the results of later processing (for example, edge detection on an image). Median filtering is very widely used in digital image processing because, under certain conditions, it preserves edges while removing noise (but see the discussion below), also having applications in signal processing.

[Implementation of median filtering](https://github.com/MeitanteiAshour/IPApps/blob/master/median_filtering.py)

## Average filtering

Average (or mean) filtering is a method of 'smoothing' images by reducing the amount of intensity variation between neighbouring pixels. The average filter works by moving through the image pixel by pixel, replacing each value with the average value of neighbouring pixels, including itself

[Implementation of Average filtering](https://github.com/MeitanteiAshour/IPApps/blob/master/average_filter.py)

## Contrast stretching

Contrast stretching (often called normalization) is a simple image enhancement technique that attempts to improve the contrast in an image by 'stretching' the range of intensity values it contains to span a desired range of values, the full range of pixel values that the image type concerned allows.

[Implementation of contrast stretching](https://github.com/MeitanteiAshour/IPApps/blob/master/contrast_streching.py)

## Histogram equalization

This method usually increases the global contrast of many images, especially when the usable data of the image is represented by close contrast values. Through this adjustment, the intensities can be better distributed on the histogram. This allows for areas of lower local contrast to gain a higher contrast. Histogram equalization accomplishes this by effectively spreading out the most frequent intensity values.

The method is useful in images with backgrounds and foregrounds that are both bright or both dark. In particular, the method can lead to better views of bone structure in x-ray images, and to better detail in photographs that are over or under-exposed. A key advantage of the method is that it is a fairly straightforward technique and an invertible operator. So in theory, if the histogram equalization function is known, then the original histogram can be recovered. The calculation is not computationally intensive. A disadvantage of the method is that it is indiscriminate. It may increase the contrast of background noise, while decreasing the usable signal.

[Implementation of Histogram equalization](https://github.com/MeitanteiAshour/IPApps/blob/master/histogram_equilization.py)

## Unsharp masking

Unsharp masking, despite what the name may suggest, is a processing technique used to sharpen images, that is to make to make edges and interfaces in your image look crisper which is often available in digital image processing software. Its name derives from the fact that the technique uses a blurred, or "unsharp", negative image to create a mask of the original image.

[Implementation on unsharp masking](https://github.com/MeitanteiAshour/IPApps/blob/master/unsharp_masking.py)
