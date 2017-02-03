#-*-coding:utf-8 -*-
from PIL import Image
import argparse


parser=argparse.ArgumentParser()#创建解析对象
parser.add_argument("file")#添加命令行参数 输入文件
parser.add_argument('-o','--output')#输出文件
parser.add_argument('--width',type=int,default=40)#输出字符画宽；
parser.add_argument('--height',type=int,default=40)#s输出字符画高

#获取参数
args=parser.parse_args()


IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output

#字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)#创建图像加载对象
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)#变更图像大小，并形成加载对象；

    txt = ""#创建字符串

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))#getpixel返回值是该象像点的RGB值,注意里面传入的是点对象；*作用是将返回rgba依次赋值给函数的形参；
        txt += '\n'

    print txt

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)