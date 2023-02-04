import glob, random

from PIL import Image
import utils

IMAGE_SIZE = 16

def get_near_clr_img(r: int,g: int,b: int, avrgs: list) -> int:
    dis = 196608
    rr, rg, rb = 0, 0, 0

    for avrg in avrgs:
        ar, ag, ab = avrg
        crt_dis = (ar - r)**2 + (ag - g)**2 + (ab - b)**2
        if dis > crt_dis:
            dis = crt_dis
            rr = ar
            rg = ag
            rb = ab
    return rr * 1000000 + rg * 1000 + rb



def main():
    target_img = Image.open("target5.jpg")
    target_img = target_img.resize((int(target_img.size[0] / 5), int(target_img.size[1] / 5)))
    target_img.show()
    image_pathes = glob.glob("images/icons/*.png")
    image_avrgs = []
    images = []

    gen_img = Image.new("RGB", (target_img.size[0] * IMAGE_SIZE, target_img.size[1] * IMAGE_SIZE), (0, 0, 0))

    avrg_obj = {}

    count = 0
    for path in image_pathes:
        img = utils.get_crop_img(Image.open(path), IMAGE_SIZE)
        avrg = utils.get_rgb_avrg(img)
        images.append(img)
        image_avrgs.append(avrg)

        if avrg_obj.get(utils.rgb_to_key(avrg[0], avrg[1], avrg[2])) == None:
            avrg_obj[utils.rgb_to_key(avrg[0], avrg[1], avrg[2])] = [count]
        else:
            avrg_obj[utils.rgb_to_key(avrg[0], avrg[1], avrg[2])].append(count)
        count += 1

    for y in range(target_img.size[1]):
        for x in range(target_img.size[0]):
            r, g, b = target_img.getpixel((x, y))
            key = get_near_clr_img(r, g, b, image_avrgs)
            pxl_img = images[random.choice(avrg_obj[key])]
            gen_img.paste(pxl_img, [x * IMAGE_SIZE, y * IMAGE_SIZE])

    gen_img.save("image.png")



if __name__ == "__main__":
    main()