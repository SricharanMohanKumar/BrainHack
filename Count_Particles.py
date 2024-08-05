import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

def Count_Particles(image, output_path):
    # Find contours
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_blobs = len(contours)
    
    total_radius = 0  # Variable to store the sum of all radii
    
    # Iterate through each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the area is small, ignore it (remove noise)
        if area < 10:
            continue

        # Get the minimum enclosing circle
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        
        total_radius += radius  # Add the radius to the total

        # Draw a circle around the contour
        cv2.circle(image, center, radius, (0, 255, 0), 1)
    
    # Calculate the average radius in millimeters
    if num_blobs > 0:
        average_radius_pixels = total_radius / num_blobs
        average_radius_mm = average_radius_pixels * 0.1  # Convert to millimeters
    else:
        average_radius_mm = 0
    
    # Save the modified image
    cv2.imwrite(output_path, image)
    
    return num_blobs, average_radius_mm

def process_images(thresholded_folder, bound_folder):
    # Create the bound folder if it doesn't exist
    if not os.path.exists(bound_folder):
        os.makedirs(bound_folder)
    
    # List all files in the thresholded folder
    thresholded_files = os.listdir(thresholded_folder)
    
    # Initialize lists to store results
    file_names = []
    num_particles_list = []
    avg_radius_list = []
    
    # Process each image
    for thresholded_file in thresholded_files:
        # Check if the file is an image (ending with .png)
        if thresholded_file.endswith('.png'):
            # Construct the full path of the thresholded image
            thresholded_image_path = os.path.join(thresholded_folder, thresholded_file)
            
            # Read the thresholded image
            thresholded_image = cv2.imread(thresholded_image_path)
            
            # Process the image and get number of particles and average radius
            output_path = os.path.join(bound_folder, thresholded_file.replace('.png', '_bound.png'))
            num_particles, avg_radius = Count_Particles(thresholded_image, output_path)
            
            # Append results to lists
            file_names.append(thresholded_file)
            num_particles_list.append(num_particles)
            avg_radius_list.append(avg_radius)
            
            print(f"Processed image: {thresholded_file} --> Bounded image saved as: {output_path}")
    
    # Display the results as a table
    print("\nResults:")
    print("{:<20} {:<20} {:<20}".format("File Name", "Number of Particles", "Average Radius (mm)"))
    for file_name, num_particles, avg_radius in zip(file_names, num_particles_list, avg_radius_list):
        print("{:<20} {:<20} {:<20}".format(file_name, num_particles, avg_radius))

# Example usage:
thresholded_folder = '/Users/sricharanmohankumar/BrainHack-1/ThresholdedImages'
bound_folder = '/Users/sricharanmohankumar/BrainHack-1/Bound'
process_images(thresholded_folder, bound_folder)
