import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/sricharanmohankumar/BrainHack-1/Images/TIssues.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range for purple color in HSV
lower_purple = np.array([120, 25, 25])  
upper_purple = np.array([165, 255, 255])

# Create a mask for purple color
mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

# Extract the purple spots
purple_spots = cv2.bitwise_and(image, image, mask=mask_purple)

# Convert the purple spots to grayscale
purple_spots_gray = cv2.cvtColor(purple_spots, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
purple_spots_gray_inverted = cv2.bitwise_not(purple_spots_gray)

# Save the output image
cv2.imwrite('Nucleus.png', purple_spots_gray_inverted)

