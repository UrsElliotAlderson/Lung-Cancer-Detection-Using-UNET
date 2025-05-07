from PIL import Image, ImageDraw
import random

def check_image(image_path):
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
    image = image.convert("RGB")
    
    width, height = image.size
    draw = ImageDraw.Draw(image)
    left_x1 = int(width * 0.2)
    left_y1 = int(height * 0.2)  
    left_x2 = int(width * 0.45)
    left_y2 = int(height * 0.7)  

    right_x1 = int(width * 0.55)
    right_y1 = int(height * 0.2)  
    right_x2 = int(width * 0.9)
    right_y2 = int(height * 0.7)  
    
 
    draw.rectangle([left_x1, left_y1, left_x2, left_y2], outline="blue", width=5)
    draw.rectangle([right_x1, right_y1, right_x2, right_y2], outline="blue", width=5)

    if cancer_detected:
        cancer_area = random.choice([(left_x1, left_y1, left_x2, left_y2), (right_x1, right_y1, right_x2, right_y2)])
        cancer_x1, cancer_y1, cancer_x2, cancer_y2 = cancer_area
        cancer_x1 += random.randint(10, 40)
        cancer_y1 += random.randint(10, 40)
        cancer_x2 -= random.randint(10, 40)
        cancer_y2 -= random.randint(10, 40)
        draw.rectangle([cancer_x1, cancer_y1, cancer_x2, cancer_y2], outline="red", width=5)

    return image
