# -*- coding:utf-8 -*-

from PIL import Image
from glob import glob
def convert(content,w,h):
    # 计算中心坐标，xml文件中使用(左上角坐标，右下角坐标)标定一个框，需要转换为中心坐标，宽、高的形式
    tempa = content[1]
    tempb = content[2]
    content[1] = str(((float(content[1]) + float(content[3]) )/ 2.0)/float(w))
    content[2] = str(((float(content[2]) + float(content[4]) )/ 2.0)/float(h))
    # 计算宽高
    content[3] = str((float(content[3]) - float(tempa))/float(w))
    content[4] = str((float(content[4]) - float(tempb))/float(h))
    return content
if __name__ == '__main__':
    fileName=glob("./data/*"+".txt")
    for i in fileName:
        print(i)
        s=open(i,'r')
        while True:
            content = s.readline()
            if content == "":
                break
            content = content.strip().split()

            content.pop(0)
            content[0] = "0"
            # 使用pillow读取图片，获取图片的宽和高
            img_pillow = Image.open("./image"+i[6:-4]+".jpg")
            img_width = img_pillow.width  # 图片宽度
            img_height = img_pillow.height  # 图片高度
            s1=open("./newdata/"+i[6:],'w')
            s1.write(" ".join(convert(content,img_width,img_height)))
            s1.close()

