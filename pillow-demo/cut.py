from PIL import Image

def cut_nice(img):
    '''
    将图片切割成 9 等分
    '''
    w = int(img.width / 3)
    img_list = []
    for i in range(3):
        for j in range(3):
            # 九等分每张图片的范围，由左上角点和右下角点两个点确定矩形区域
            img_area_coord = (j*w, i*w, (j+1)*w, (i+1)*w)
            # img.crop() 将区域切割成单独的图片
            img_area = img.crop(img_area_coord)
            img_list.append(img_area)
    return img_list


def to_square(img):
    '''
    给图片短边补齐，变成一个正方形
    '''
    width = img.width
    height = img.height

    if width > height:
        # 宽 > 高，高补齐
        bg_img = Image.new('RGB', (width, width), (255, 255, 255))
        bg_img.paste(img, (0, int((width - height) / 2)))
    else:
        # 高 > 宽，宽补齐
        bg_img = Image.new('RGB', (height, height), (255, 255, 255))
        bg_img.paste(img, (int((height - width) / 2)), 0)
    return bg_img


def save_multi(img_list, img_format):
    '''
    批量保存图片
    '''
    for index, img in enumerate(img_list):
        img.save(str(index) + '.' + img_format)

def main(img_file):
    # 获取源图片
    img = Image.open(img_file)
    # 图片格式 JPEG
    img_format = img.format  

    if img.width == img.height:
        img_list = cut_nice(img)
    else:
        new_img = to_square(img)
        img_list = cut_nice(new_img)

    # 批量保存图片
    save_multi(img_list, img_format)

img_file = 'pillow_cut_01.jpg'
main(img_file)