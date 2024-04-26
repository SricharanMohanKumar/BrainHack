import cv2
import matplotlib.pyplot as plt

def Count_Particles(image):
    # Find contours
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the area is small, ignore it (remove noise)
        if area < 10:
            continue

        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a rectangle around the contour
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    # Display the result
    plt.imshow(image, cmap='gray')



