from PIL import Image, ImageDraw

def pixel2char(pixel):
    '''
    像素转字符
    '''
    # 前面的值占位大点，越往后，占位越少
    chars = '@B%8&WM#*ABUNHKPQWMASDFGHJKLZZCVUNXRJFT/\|{}1()[]?i-_+~<>I!1::,.\.'
    # 像素值越大，取 chars 后面的字符
    char = chars[int(pixel / 255 * (len(chars) - 1))]
    return char

def str2img(str):
    '''
    字符串转图片
    '''
    img = Image.new('RGB', (2400, 3200), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), str, fill='black')
    return img

def main(file_name):
    # 读取图片
    img = Image.open(file_name)

    # 转成灰度图
    img = img.convert('L')
    (width, height) = (int(img.width), (int(img.height)))
    img = img.resize((width, height))

    # img.getpixel((0, 0))  255  白色
    text = ''
    for y in range(img.height):
        for x in range(img.width):
            text += pixel2char(img.getpixel((x, y)))
        text += '\n'

    img = str2img(text)
    img.save('pillow_char_02.png')

file_name = "pillow_char.png"
main(file_name)