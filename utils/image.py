from PIL import Image
import os
def image_resize(img_path,max_size=(500, 500)):
    if not img_path or not os.path.exists(img_path):
        return
    img = Image.open(img_path)
    if img.height > max_size[0] or img.width > max_size[1]:
        img.thumbnail(max_size)
        img.save(img_path)