import cv2
import matplotlib.pyplot as plt
import Count_Particles as cp

def thresholding(image,value):
# Read the grayscale image
    image_to_treshold = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # Set threshold value
    threshold_value = value  # You can adjust this value as per your requirement

    # Apply thresholding
    ret, thresholded_image = cv2.threshold(image_to_treshold, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imwrite('thresholded_image.png', thresholded_image)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    cp.Count_Particles(thresholded_image)

image= 'grayscale_image.png'
value = 150
thresholding(image, value)
