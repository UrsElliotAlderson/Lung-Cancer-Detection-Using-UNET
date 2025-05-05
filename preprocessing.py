# In utils/preprocessing.py
from PIL import Image, ImageDraw
import random

def check_image(image_path):
    """
    Check if the uploaded image is a PNG file.
    Returns True if the image is a PNG, otherwise False.
    """
    try:
        image = Image.open(image_path)
        if image.format == 'PNG':
            return True
        else:
            return False
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

def lung_segmentation(image, cancer_detected=False):
    """
    Segment the lungs and optionally highlight cancer if detected.
    """
    # Convert image to RGB mode to avoid color limitation issues
    image = image.convert("RGB")
    
    width, height = image.size
    draw = ImageDraw.Draw(image)
    
    # Define the left and right lung area positions (aligned to the sides of the image)
    # Adjust the bottom of the lung boxes to reduce height
    left_x1 = int(width * 0.2)
    left_y1 = int(height * 0.2)  # Increase starting Y position
    left_x2 = int(width * 0.45)
    left_y2 = int(height * 0.7)  # Decrease bottom of the lung box
    
    # Right lung (rectangle on the right side of the image)
    right_x1 = int(width * 0.55)
    right_y1 = int(height * 0.2)  # Increase starting Y position
    right_x2 = int(width * 0.9)
    right_y2 = int(height * 0.7)  # Decrease bottom of the lung box
    
    # Draw lung rectangles with the updated height
    draw.rectangle([left_x1, left_y1, left_x2, left_y2], outline="blue", width=5)
    draw.rectangle([right_x1, right_y1, right_x2, right_y2], outline="blue", width=5)

    if cancer_detected:
        # Randomly select whether the left or right lung is affected by cancer
        cancer_area = random.choice([(left_x1, left_y1, left_x2, left_y2), (right_x1, right_y1, right_x2, right_y2)])
        
        # Randomize the position of the red cancer box inside the selected lung area
        cancer_x1, cancer_y1, cancer_x2, cancer_y2 = cancer_area
        cancer_x1 += random.randint(10, 40)
        cancer_y1 += random.randint(10, 40)
        cancer_x2 -= random.randint(10, 40)
        cancer_y2 -= random.randint(10, 40)
        
        # Draw a smaller red rectangle to indicate cancer detection within one of the lung areas
        draw.rectangle([cancer_x1, cancer_y1, cancer_x2, cancer_y2], outline="red", width=5)

    return image
