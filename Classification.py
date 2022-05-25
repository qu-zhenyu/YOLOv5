# 根据图像类别标签，将同属一类的图像移动至对应的子文件夹中
import os
import shutil
import xml.dom.minidom
from typing import List

from PIL import Image

# -------------------提前创建文件夹，用于存放图片类别---------------------#
filename = 'model_data/predefined_classes.txt'
with open(filename, encoding='utf-8') as f_obj:
    val_list = f_obj.read()
class_names = val_list.split('\n')  # 需根据自己的类别设置


root_dir = os.path.dirname(__file__)
images_path = os.path.join('WAdevikit', 'xml_class')
for class_name in class_names:
    class_dir = os.path.join(images_path, class_name)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)
# -------------------------------------------------------------------------#

AnnoPath = r'VOCdevkit_empty\\VOC2007\\Annotations\\'  # 标签文件路径
imgPath = r'VOCdevkit_empty\\VOC2007\\JPEGImages\\'  # 图片文件路径
Annolist = os.listdir(AnnoPath)
rate = {}  # 创建一个字典用于存放标签名和对应的出现次数
total = 0

for annotation in Annolist:
    fullname = AnnoPath + annotation
    print(fullname, annotation)
    image_name = annotation.split('.')[0]
    # print(image_name)

    dom = xml.dom.minidom.parse(fullname)  # 打开XML文件
    # print(fullname,annotation)
    print('---------------', total)

    collection = dom.documentElement  # 获取元素对象
    objectlist = collection.getElementsByTagName('object')  # 获取标签名为object的信息
    for object in objectlist:
        namelist = object.getElementsByTagName('name')  # 获取子标签name的信息
        objectname = namelist[0].childNodes[0].data  # 取到name具体的值
        if objectname not in rate:  # 判断字典里有没有标签，如无添加相应字段
            rate[objectname] = 0

        # ----------------------拷贝图片到对应目录------------------------#
        image_path = imgPath + '/' + image_name + ".jpg"
        # print(image_path)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            # 添加判断逻辑
            jpg_ = os.path.join(images_path, objectname) + '/' + image_name + ".jpg"
            if os.path.exists(jpg_) is False:
                image.save(os.path.join(images_path, objectname) + '/' + image_name + ".jpg")
                # print(os.path.join(images_path, objectname) +'/'+image_name+".jpg")
        # ----------------------------------------------------------------#
        # ----------------------拷贝xml文件到对应目录------------------------#
        anno_path = AnnoPath + image_name + ".xml"
        # print(anno_path)
        xml_path = 'WAdevikit/xml_class/'
        # print(image_path)
        # print(os.path.exists(image_path))
        if os.path.exists(anno_path):
            # image = Image.open(image_path)
            # print('1')
            old = os.path.join(xml_path, objectname) + '/' + image_name + ".xml"
            shutil.copyfile(anno_path, old)
            # print(os.path.join(xml_path, objectname)+'/'+image_name+".xml")
            # image.save(os.path.join(images_path, objectname) +'/'+image_name+".jpg")
        # ----------------------------------------------------------------#

        rate[objectname] += 1
        total += 1

print(rate)
print(total)
