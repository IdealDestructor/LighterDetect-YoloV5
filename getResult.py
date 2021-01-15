# -*- coding:utf-8 -*-
from decimal import Decimal
from PIL import Image
from glob import glob
def convert(content,w,h):
    tempa = Decimal(content[2]).quantize(Decimal('0.000000'))*w
    tempb = Decimal(content[3]).quantize(Decimal('0.000000'))*h
    tempc = Decimal(content[4]).quantize(Decimal('0.000000'))*w/2
    tempd = Decimal(content[5]).quantize(Decimal('0.000000'))*h/2
    content[2] = str(Decimal(Decimal(str(tempa))-Decimal(str(tempc))).quantize(Decimal('0.0')))
    content[3] = str(Decimal(Decimal(str(tempb))-Decimal(str(tempd))).quantize(Decimal('0.0')))
    content[4] = str(Decimal(Decimal(str(tempa))+Decimal(str(tempc))).quantize(Decimal('0.0')))
    content[5] = str(Decimal(Decimal(str(tempb))+Decimal(str(tempd))).quantize(Decimal('0.0')))
    return content
if __name__ == '__main__':
    fileName=glob("./reslabels/*"+".txt")
    for i in fileName:
        print(i)
        s=open(i,'r')
        s1=open("./result.txt",'a')
        while True:
            content = s.readline()
            if content == "":
                break
            content = content.strip().split()
            content[0] = str(i[12:-4])
            temp = content[5]
            content[5] = content[4]
            content[4] = content[3]
            content[3] = content[2]
            content[2] = content[1]
            content[1] = str(Decimal(temp).quantize(Decimal('0.000')))
            # 使用pillow读取图片，获取图片的宽和高
            img_pillow = Image.open("./testimages"+i[11:-4]+".jpg")
            img_width = img_pillow.width  # 图片宽度
            img_height = img_pillow.height  # 图片高度
            s1.write(" ".join(convert(content,img_width,img_height))+'\n')
        s1.close()

