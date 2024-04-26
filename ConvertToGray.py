import matplotlib.pyplot as plt
from PIL import Image

def convert_to_grayscale(image_path):
    # Load the image
    img = Image.open(image_path)
    
    # Convert to grayscale
    grayscale_image = img.convert("L")
    
    # Save the grayscale image
    grayscale_image_path = image_path.replace('.png', '_grayscale.png')
    grayscale_image.save(grayscale_image_path)
    
    # Display the original and grayscale images
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    
    plt.show()
    
    # Close the images
    img.close()
    grayscale_image.close()

# Example usage:
image_path = 'cc.png'
convert_to_grayscale(image_path)
