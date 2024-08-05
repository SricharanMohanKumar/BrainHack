import os
import matplotlib.pyplot as plt
from PIL import Image

def convert_images_to_grayscale(images_folder, grayscale_folder):
    # Create the grayscale folder if it doesn't exist
    if not os.path.exists(grayscale_folder):
        os.makedirs(grayscale_folder)
    
    # List all files in the images folder
    image_files = os.listdir(images_folder)
    
    # Process each image
    for image_file in image_files:
        # Check if the file is an image (ending with .png)
        if image_file.endswith('.png'):
            # Construct the full path of the image
            image_path = os.path.join(images_folder, image_file)
            
            # Load the image
            img = Image.open(image_path)
            
            # Convert to grayscale
            grayscale_image = img.convert("L")
            
            # Construct the path for saving the grayscale image
            grayscale_image_path = os.path.join(grayscale_folder, image_file.replace('.png', '_grayscale.png'))
            
            # Save the grayscale image
            grayscale_image.save(grayscale_image_path)
            
            # Close the images
            img.close()
            grayscale_image.close()

            print(f"Processed image: {image_file} --> Grayscale image saved as: {grayscale_image_path}")

# Example usage:
images_folder = '/Users/sricharanmohankumar/BrainHack-1/Images'
grayscale_folder = '/Users/sricharanmohankumar/BrainHack-1/Grayscale'
convert_images_to_grayscale(images_folder, grayscale_folder)
