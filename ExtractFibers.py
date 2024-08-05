import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/sricharanmohankumar/BrainHack-1/Images/TIssues.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range for yellow color in HSV, adjusted to include lighter yellows
lower_yellow = np.array([5, 30, 30])  # Lower the saturation and value bounds
upper_yellow = np.array([35, 255, 255])

# Create a mask for yellow color
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Apply morphological operations to enhance thin yellow stripes
kernel = np.ones((3, 3), np.uint8)
mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_CLOSE, kernel)

# Extract the yellow spots
yellow_spots = cv2.bitwise_and(image, image, mask=mask_yellow)

# Convert the yellow spots to grayscale
yellow_spots_gray = cv2.cvtColor(yellow_spots, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
yellow_spots_gray_inverted = cv2.bitwise_not(yellow_spots_gray)

# Save the output image
cv2.imwrite('Fibers.png', yellow_spots_gray_inverted)
