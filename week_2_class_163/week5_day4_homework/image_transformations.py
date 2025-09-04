from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from scipy.ndimage import rotate
import os

# path to the image
image_path = '/Users/spectorpower/Documents/DI_bootcamp/files/Flower Color Images Dataset/flowers/flowers/19_010.png'

# check if file exists
if not os.path.exists(image_path):
    print("File not found:", image_path)
    exit()

# load image
original_image = Image.open(image_path)

# show original image
plt.imshow(original_image)
plt.title("Original Image")
plt.axis("off")
plt.show()

# rotate image by 30 degrees
def rotate_image_30_degrees(image):
    return rotate(image, 30, reshape=True)

rotated_image = rotate_image_30_degrees(original_image)

# show rotated image
plt.imshow(rotated_image)
plt.title("Rotated 30°")
plt.axis("off")
plt.show()

# flip image horizontally and vertically
flipped_horizontally = ImageOps.mirror(original_image)
flipped_vertically = ImageOps.flip(original_image)

# show flipped images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(flipped_horizontally)
plt.title("Horizontally Flipped")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(flipped_vertically)
plt.title("Vertically Flipped")
plt.axis("off")

plt.show()

# zoom image (scale by 1.2x)
width, height = original_image.size
zoomed_image = original_image.resize((int(width * 1.2), int(height * 1.2)))

# show zoomed image
plt.imshow(zoomed_image)
plt.title("Zoomed Image (1.2x)")
plt.axis("off")
plt.show()
