import os
import numpy as np
import codecs
import pandas as pd
import json
from glob import glob
import cv2
import shutil
from sklearn.model_selection import train_test_split
from IPython import embed
#1.标签路径
csv_file = "/4TB-HDD1/lsc/data/kaggle/xray_det/train.csv"
saved_path = "/4TB-HDD1/lsc/data/kaggle/xray_det/"                #保存路径
image_save_path = "/4TB-HDD1/lsc/data/kaggle/xray_det/"
image_raw_path = "/4TB-HDD1/lsc/data/kaggle/xray_det/voc/train/"
#2.创建要求文件夹
if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")

#3.获取待处理文件
total_csv_annotations = {}
annotations = pd.read_csv(csv_file,header=None).values[1:]
# print(annotations[0][0])
for annotation in annotations:
    # print(annotation)
    key = annotation[0].split(os.sep)[-1]
    # key = annotation[0]
    value = np.array([annotation[1:]])
    if key in total_csv_annotations.keys():
        total_csv_annotations[key] = np.concatenate((total_csv_annotations[key],value),axis=0)
    else:
        total_csv_annotations[key] = value

# print(total_csv_annotations.items())

#4.读取标注信息并写入 xml
for filename,label in total_csv_annotations.items():
    #embed()
    print(image_raw_path + filename + '.jpg')
    height, width, channels = cv2.imread(image_raw_path + filename + '.jpg').shape
    #embed()
    with codecs.open(saved_path + "Annotations/"+filename.replace(".jpg",".xml"),"w","utf-8") as xml:
        xml.write('<annotation>\n')
        xml.write('\t<folder>' + 'VOC2007' + '</folder>\n')
        xml.write('\t<filename>' + filename + '</filename>\n')
        xml.write('\t<source>\n')
        xml.write('\t\t<database>kaggle xray</database>\n')
        xml.write('\t\t<annotation>kaggle xray</annotation>\n')
        xml.write('\t\t<image>flickr</image>\n')
        xml.write('\t\t<flickrid>NULL</flickrid>\n')
        xml.write('\t</source>\n')
        xml.write('\t<owner>\n')
        xml.write('\t\t<flickrid>NULL</flickrid>\n')
        xml.write('\t\t<name>Klawens</name>\n')
        xml.write('\t</owner>\n')
        xml.write('\t<size>\n')
        xml.write('\t\t<width>'+ str(width) + '</width>\n')
        xml.write('\t\t<height>'+ str(height) + '</height>\n')
        xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
        xml.write('\t</size>\n')
        xml.write('\t\t<segmented>0</segmented>\n')
        if isinstance(label,float):
            ## 空白
            xml.write('</annotation>')
            continue
        for label_detail in label:
            labels = label_detail
            #embed()
            xmin = int(labels[0])
            ymin = int(labels[1])
            xmax = int(labels[2])
            ymax = int(labels[3])
            label_ = labels[-1]
            # xmin = 0 if labels[0] is None else labels[0]
            # ymin = 0 if labels[1] is None else labels[1]
            # xmax = 1 if labels[2] is None else labels[2]
            # ymax = 1 if labels[3] is None else labels[3]
            # label_ = labels[-1]
            if xmax <= xmin:
                pass
            elif ymax <= ymin:
                pass
            else:
                xml.write('\t<object>\n')
                xml.write('\t\t<name>'+label_+'</name>\n')
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>1</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')
                print(filename,xmin,ymin,xmax,ymax,labels)
        xml.write('</annotation>')
        

#6.split files for txt
txtsavepath = saved_path + "ImageSets/Main/"
ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')
total_files = glob(saved_path+"./Annotations/*.xml")
total_files = [i.split("/")[-1].split(".xml")[0] for i in total_files]
#test_filepath = ""
for file in total_files:
    ftrainval.write(file + "\n")

# move images to voc JPEGImages folder
for image in glob(image_raw_path+"/*.jpg"):
    shutil.copy(image,saved_path+image_save_path)

train_files,val_files = train_test_split(total_files,test_size=0.15,random_state=42)

for file in train_files:
    ftrain.write(file + "\n")
#val
for file in val_files:
    fval.write(file + "\n")

ftrainval.close()
ftrain.close()
fval.close()
#ftest.close()



    