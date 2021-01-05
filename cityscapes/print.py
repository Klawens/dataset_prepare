import os
import cv2
import numpy as np
names = os.listdir('../data/trainid/')   # 图片路径
dic={}
for i in range(34):
    if i<7:
        dic[i]=255
    elif i<11:
        dic[i]=0
    elif i<17:
        dic[i]=1
    elif i<21:
        dic[i]=2
    elif i<23:
        dic[i]=3
    elif i<24:
        dic[i]=4
    elif i<26:
        dic[i]=5
    else:
        dic[i]=6
dic[-1]=6
for i,name in enumerate(names):
    print(i)
    # if i==10:
        # break
    img = cv2.imread("../data/trainid/{}".format(name))
    for j in range(-1,34,1):
        img[img==j]=dic[j]
    cv2.imwrite('data/{}'.format(name),img)