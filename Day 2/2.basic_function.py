import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy (not used here, but commonly needed in CV tasks)

# ### 1. Convert to gray scale

# # Read the image from file
# img = cv2.imread('resources/lena.png')

# # Convert the color image to grayscale
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Print the shapes of the color and grayscale images

# print("Color_img Shape: ", img.shape)      # Expected: (height, width, 3)
# print("img_gray Shape: ", img_gray.shape)  # Expected: (height, width)

# # Display both the original and grayscale images
# cv2.imshow("Color_img", img)
# cv2.imshow("Gray_img", img_gray)

# # Wait indefinitely until a key is pressed

# cv2.waitKey(0)


# ### 2. Convert to blur

# # Read the image
# img = cv2.imread('resources/lena.png')

# # Convert to grayscale
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian Blur to the grayscale image
# # (7,7) is the kernel size and 0 is the standard deviation
# img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)

# # Print shapes
# print("Color_img Shape: ", img.shape)
# print("img_gray Shape: ", img_gray.shape)

# # Display all versions
# cv2.imshow("Color_img", img)
# cv2.imshow("Gray_img", img_gray)
# cv2.imshow("img_blur", img_blur)

# # Wait for key press
# cv2.waitKey(0)


### 3. Convert to Canny edge image

# Read the image
img = cv2.imread('resources/lena.png')

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)

# Perform Canny edge detection
# Thresholds 100 and 100 can be adjusted for edge sensitivity
img_canny = cv2.Canny(img_blur, 100, 100)

# Print image shapes
print("Color_img Shape: ", img.shape)
print("img_gray Shape: ", img_gray.shape)

# Show original, grayscale, blurred, and canny edge images
cv2.imshow("Color_img", img)
cv2.imshow("Gray_img", img_gray)
cv2.imshow("img_blur", img_blur)
cv2.imshow("img_canny", img_canny)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)
