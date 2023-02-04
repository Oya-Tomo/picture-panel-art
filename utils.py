from PIL import Image

def get_rgb_avrg(image: Image) -> tuple:
    r, g, b = 0, 0, 0
    data = image.getdata()
    for pxl in data:
        r += pxl[0]
        g += pxl[1]
        b += pxl[2]
    length = len(data)
    return int(r / length), int(g / length), int(b / length)

def get_crop_img(image: Image, size: int) -> Image:
    w, h = image.size
    if w < h:
        image = image.crop((0, (h - w)/2, w, (h + w)/2))
    else:
        image = image.crop(((w - h)/2, 0, (w + h)/2, h))
    image = image.resize((size, size))
    return image

def rgb_to_key(r, g, b) -> int:
    return r * 1000000 + g * 1000 + b