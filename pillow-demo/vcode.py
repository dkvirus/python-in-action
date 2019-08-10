'''
1. 创建一张空白图片 200px * 50px
2. 随机创建 4 个字符，大写字母、小写字母、数字
3. 每个字符要给随机的颜色
4. 将字符添加到图片上
'''

from PIL import Image, ImageDraw, ImageFont
from random import choice, sample

def random_char():
    '''
    生成随机字符：大写字母、小写字母、数值
    ASCII
    65-90    A-Z
    97-122   a-z
    48-57    0-9
    '''
    chars = []
    chars.extend([i for i in range(65, 91)])
    chars.extend([i for i in range(97, 123)])
    chars.extend([i for i in range(48, 58)])
    random_char = choice(chars)
    char = chr(random_char)

    return char

def random_char_color():
    '''
    给随机字符生成个随机颜色
    '''
    return tuple(sample(range(50, 120), 3))

def gene_vcode():
    '''
    生成验证码图片
    1. 创建 200 * 50 的图片
    '''

    width = 200
    height = 50
    im = Image.new('RGB', (width, height), (0, 0, 0))

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Arial", 30)

    for i in range(4):
        draw.text((i * 50 + 10, 7), random_char(), font= font, fill=random_char_color())

    im.show()

gene_vcode()



'''
random.choice([1, 2, 3])   随机返回列表中的一个值
random.randint(100, 200)    随机返回 100-200 范围内的一个整数
random.sample(range(100, 200), 3)   随机返回100-200范围内三个整数

im = Image.new(模式, (宽, 高), 颜色)    创建个图像
im.show() 显示图像
draw = ImageDraw(im)    创建绘画对象
draw.point((x, y), fill=颜色)        画点，(x, y) 表示要画点的坐标
my_font = ImageFont.truetype('arial.ttf', 36)     (字体, 大小)
draw.text((x, y), 文字, font=字体, fill=颜色)     写文字，(x, y) 文字左上角坐标点
'''