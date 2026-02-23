from PIL import Image

def image_resize(img_path, max_size=(500, 500)):
    img = Image.open(img_path)
    if img.height > max_size[0] or img.width > max_size[1]:
        img.thumbnail(max_size)
        img.save(img_path)