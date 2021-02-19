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

## Sobel operator

The Sobel operator, sometimes called the Sobel–Feldman operator or Sobel filter, is used in image processing and computer vision, particularly within edge detection algorithms where it creates an image emphasising edges. It is named after Irwin Sobel and Gary Feldman, colleagues at the Stanford Artificial Intelligence Laboratory (SAIL). Sobel and Feldman presented the idea of an "Isotropic 3x3 Image Gradient Operator" at a talk at SAIL in 1968.Technically, it is a discrete differentiation operator, computing an approximation of the gradient of the image intensity function. At each point in the image, the result of the Sobel–Feldman operator is either the corresponding gradient vector or the norm of this vector. The Sobel–Feldman operator is based on convolving the image with a small, separable, and integer-valued filter in the horizontal and vertical directions and is therefore relatively inexpensive in terms of computations. On the other hand, the gradient approximation that it produces is relatively crude, in particular for high-frequency variations in the image.

[Sobel Implementation](https://github.com/MeitanteiAshour/IPApps/blob/master/sobel_op.py)
