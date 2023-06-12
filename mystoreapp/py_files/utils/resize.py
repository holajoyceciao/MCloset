import os
from PIL import Image
import glob

img_dir = '../../static/img/product'
output_dir = '../../static/img/resize_product'
desired_size = (1700, 2550)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

images = glob.glob(img_dir + "/*.jpg") 

for img_path in images:
    img = Image.open(img_path)
    img_resized = img.resize(desired_size, Image.ANTIALIAS)
    output_path = os.path.join(output_dir, os.path.basename(img_path))
    img_resized.save(output_path)

print(f"All images have been resized to {desired_size}!")
