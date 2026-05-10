"""
========================================================
OpenCV Basics level 01
========================================================

Topics:
1. Read Image
2. Check Image Information
3. Resize Image
4. Convert to Grayscale
5. Save Image
6. Access Pixels
7. Change Pixel Colors
8. Draw Shapes
9. Put Text on Image
10. Crop Image
11. Flip Image
12. Blur Image
13. Edge Detection
14. Rotate Image
15. Webcam Capture

Important:
OpenCV reads images as:
    BGR  -> Blue Green Red
NOT:
    RGB  -> Red Green Blue
"""

import cv2
import numpy as np

# ========================================================
# [1] READ IMAGE
# ========================================================

"""
cv2.imread(path, flag)

Flags:
    cv2.IMREAD_COLOR      -> Default color image
    cv2.IMREAD_GRAYSCALE  -> Read as grayscale
    cv2.IMREAD_UNCHANGED  -> Keep all channels

Returns:
    Image as NumPy Array
"""

image = cv2.imread("images/bird01.png")

# Display image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# ========================================================
# [2] CHECK IMAGE INFORMATION
# ========================================================

"""
image.shape returns:
    (height, width, channels)

Example:
    (720, 1280, 3)

3 channels means:
    Blue
    Green
    Red
"""

print("Image Shape:", image.shape)

height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]

print("Height :", height)
print("Width  :", width)
print("Channels:", channels)

"""
Other useful properties:
"""

print("Image Size (Total Pixels):", image.size)
print("Data Type:", image.dtype)

# ========================================================
# [3] RESIZE IMAGE
# ========================================================

"""
cv2.resize(image, (width, height))

Important:
    Size order is:
        (width, height)

Interpolation options:
    cv2.INTER_LINEAR   -> Default / good for enlarging
    cv2.INTER_AREA     -> Best for shrinking
    cv2.INTER_CUBIC    -> Higher quality
"""

resized = cv2.resize(
    image,
    (300, 300),
    interpolation=cv2.INTER_AREA
)

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

# ========================================================
# [4] CONVERT TO GRAYSCALE
# ========================================================

"""
Why grayscale?

Benefits:
    - Faster processing
    - Less memory
    - Easier edge detection
    - Easier face detection

Used in:
    AI
    Computer Vision
    OCR
"""

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray)
cv2.waitKey(0)

# ========================================================
# [5] SAVE IMAGE
# ========================================================

"""
cv2.imwrite(output_path, image)
"""

cv2.imwrite("images/output_gray.jpg", gray)

print("Gray image saved successfully.")

# ========================================================
# [6] ACCESS PIXELS
# ========================================================

"""
Access format:
    image[y, x]

Returns:
    [B, G, R]
"""

pixel = image[100, 200]

print("Pixel Value:", pixel)

blue = pixel[0]
green = pixel[1]
red = pixel[2]

print("Blue :", blue)
print("Green:", green)
print("Red  :", red)

# ========================================================
# [7] CHANGE PIXEL COLORS
# ========================================================

"""
Change specific pixel:
    image[y, x] = [B, G, R]
"""

# Change pixel to pure red
image[100, 200] = [0, 0, 255]

cv2.imshow("Modified Pixel", image)
cv2.waitKey(0)

# ========================================================
# [8] DRAW SHAPES
# ========================================================

"""
--------------------------------
A) Draw Line
--------------------------------

cv2.line(
    image,
    start_point,
    end_point,
    color,
    thickness
)
"""

cv2.line(
    image,
    (50, 50),
    (300, 300),
    (0, 255, 0),
    5
)

"""
--------------------------------
B) Draw Rectangle
--------------------------------

cv2.rectangle(
    image,
    top_left,
    bottom_right,
    color,
    thickness
)

Thickness:
    positive -> border
    -1       -> filled rectangle
"""

cv2.rectangle(
    image,
    (100, 100),
    (400, 300),
    (255, 0, 0),
    3
)

"""
--------------------------------
C) Draw Circle
--------------------------------

cv2.circle(
    image,
    center,
    radius,
    color,
    thickness
)
"""

cv2.circle(
    image,
    (500, 250),
    80,
    (0, 0, 255),
    4
)

cv2.imshow("Shapes", image)
cv2.waitKey(0)

# ========================================================
# [9] PUT TEXT ON IMAGE
# ========================================================

"""
cv2.putText(
    image,
    text,
    position,
    font,
    font_scale,
    color,
    thickness
)

Common Fonts:
    cv2.FONT_HERSHEY_SIMPLEX
    cv2.FONT_HERSHEY_COMPLEX
    cv2.FONT_HERSHEY_TRIPLEX
"""

cv2.putText(
    image,
    "OpenCV Tutorial",
    (50, 450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (255, 255, 255),
    3
)

cv2.imshow("Text on Image", image)
cv2.waitKey(0)

# ========================================================
# [10] CROP IMAGE
# ========================================================

"""
Cropping:
    image[y1:y2, x1:x2]

Example:
    image[100:400, 200:500]
"""

crop = image[100:400, 200:500]

cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)

# ========================================================
# [11] FLIP IMAGE
# ========================================================

"""
cv2.flip(image, flipCode)

flipCode:
    0   -> Vertical Flip
    1   -> Horizontal Flip
    -1  -> Both Directions
"""

flipped = cv2.flip(image, 1)

cv2.imshow("Flipped Image", flipped)
cv2.waitKey(0)

# ========================================================
# [12] BLUR IMAGE
# ========================================================

"""
Why Blur?

Used for:
    - Noise reduction
    - Smoothing
    - Preprocessing

Very important before:
    - Edge detection
    - Object detection

--------------------------------
Gaussian Blur
--------------------------------

cv2.GaussianBlur(
    image,
    kernel_size,
    sigmaX
)

Kernel:
    Must be odd numbers
"""

blur = cv2.GaussianBlur(
    image,
    (17, 17),
    0
)

cv2.imshow("Blurred Image", blur)
cv2.waitKey(0)

# ========================================================
# [13] EDGE DETECTION
# ========================================================

"""
Canny Edge Detection

cv2.Canny(
    image,
    threshold1,
    threshold2
)

threshold1:
    minimum edge strength

threshold2:
    maximum edge strength
"""

edges = cv2.Canny(image, 100, 200)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

# ========================================================
# [14] ROTATE IMAGE
# ========================================================

"""
cv2.rotate(image, rotateCode)

Options:
    cv2.ROTATE_90_CLOCKWISE
    cv2.ROTATE_90_COUNTERCLOCKWISE
    cv2.ROTATE_180
"""

rotated = cv2.rotate(
    image,
    cv2.ROTATE_90_CLOCKWISE
)

cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

# ========================================================
# [15] WEBCAM CAPTURE
# ========================================================

"""
cv2.VideoCapture(0)

0 -> default camera
1 -> external camera
"""

cap = cv2.VideoCapture(0)

while True:

    # Read frame from camera
    ret, frame = cap.read()

    """
    ret:
        True  -> frame captured successfully
        False -> failed
    """

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("Webcam", frame)

    """
    waitKey(1):
        Wait 1 millisecond

    27 -> ESC key
    """

    if cv2.waitKey(1) == 27:
        break

# Release camera resources
cap.release()

# Close all windows
cv2.destroyAllWindows()
