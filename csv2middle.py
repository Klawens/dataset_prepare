import json, os, csv
import cv2

j = []
f = open('/4TB-HDD1/lsc/data/kaggle/xray_original/train.csv', 'r')
f_csv = csv.reader(f)

for row in f_csv:
    ann = {}
    dic = {}
    filename = row[0]
    size = cv2.imread('/4TB-HDD1/lsc/data/kaggle/xray_jpg/train/' + filename + '.jpg')
    if size is not None:
        width = size.shape[0]
        height = size.shape[1]
        ann['bboxes'] = [row[4], row[5], row[6], row[7]]
        ann['labels'] = [row[2]]
        dic['filename'] = filename + '.jpg'
        dic['width'] = width
        dic['height'] = height
        dic['ann'] = ann
        j.append(dic)
        print(dic)

res = open('/4TB-HDD1/lsc/data/kaggle/xray_jpg/train.json', 'w')
json.dump(j, res)
