import csv
import os
import cv2
from tqdm import tqdm

class2id = {
    'holothurian': 0,
    'echinus': 1,
    'scallop': 2,
    'starfish': 3
}

image_path = 'val/'
image_list = os.listdir(image_path)

csv_anno_ = csv.reader(open('val.csv', 'r'))

csv_anno = []
for a in csv_anno_:
    csv_anno.append(a)

for img in tqdm(image_list):
    # print(img)
    w, h = cv2.imread(image_path+img).shape[1], cv2.imread(image_path+img).shape[0]
    res = open('val_txt/{}.txt'.format(img.split('.')[0]), 'w', newline='')

    for anno in csv_anno:
        # print(anno[0], img.split('.')[0])
        if (str(anno[0]) == str(img.split('.')[0])) and anno[5] != 'waterweeds':
            res.write('{} {} {} {} {}\n'.format(class2id[anno[5]], (float(anno[1])+float(anno[3]))/2/w,
            (float(anno[2])+float(anno[4]))/2/h, (float(anno[3])-float(anno[1]))/w, (float(anno[4])-float(anno[2]))/h))

