# coding=utf-8
# from PIL import Image

# im = Image.open('./test.jpg')
# print im.format, im.size, im.mode
#
# im.thumbnail((100, 100))
# im.save('./thumb.jpg','JPEG')

# 生成验证码

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机背景颜色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 定义大小
width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('arial.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字
for t in range(4):
    draw.text((60*t+15, 10), rndChar(), font=font, fill=rndColor2())

# 对图像进行模糊处理
image = image.filter(ImageFilter.BLUR)

image.save('./code.jpg', 'jpeg')

