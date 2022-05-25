import codecs
import os

file = open('judge/val_empty.txt', 'w')
path = "judge/val_empty/"
listdir = os.listdir(path=path)
for txt in listdir:
    f = codecs.open(os.path.join(path, txt), mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
    line = f.readline()  # 以行的形式进行读取文件
    list1 = []
    while line:
        a = line.split()
        b = a[1]
        list1.append(b)
        line = f.readline()
    f.close()

    list1.sort(reverse=True)
    for i in list1:
        if 1.0 > float(i):
            file.write(i + '\n')  # 写入置信度最大值
            break
# 关闭文件
file.close()
