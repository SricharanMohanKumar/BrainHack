import os
import cv2
import matplotlib.pyplot as plt

def threshold_images(grayscale_folder, threshold_folder, threshold_value):
    # Create the threshold folder if it doesn't exist
    if not os.path.exists(threshold_folder):
        os.makedirs(threshold_folder)
    
    # List all files in the grayscale folder
    grayscale_files = os.listdir(grayscale_folder)
    
    # Process each image
    for grayscale_file in grayscale_files:
        # Check if the file is an image (ending with .png)
        if grayscale_file.endswith('.png'):
            # Construct the full path of the grayscale image
            grayscale_image_path = os.path.join(grayscale_folder, grayscale_file)
            
            # Read the grayscale image
            grayscale_image = cv2.imread(grayscale_image_path, cv2.IMREAD_GRAYSCALE)
            
            # Apply thresholding
            _, thresholded_image = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)
            
            # Construct the path for saving the thresholded image
            thresholded_image_path = os.path.join(threshold_folder, grayscale_file.replace('.png', '_thresholded.png'))
            
            # Save the thresholded image
            cv2.imwrite(thresholded_image_path, thresholded_image)
            
            print(f"Processed image: {grayscale_file} --> Thresholded image saved as: {thresholded_image_path}")

            # Display the thresholded image
            plt.figure(figsize=(10, 5))
            plt.imshow(thresholded_image, cmap='gray')
            plt.title('Thresholded Image')
            plt.axis('off')
            plt.show()

# Example usage:
grayscale_folder = '/Users/sricharanmohankumar/BrainHack-1/Grayscale'
threshold_folder = '/Users/sricharanmohankumar/BrainHack-1/ThresholdedImages'
threshold_value = 150
threshold_images(grayscale_folder, threshold_folder, threshold_value)
