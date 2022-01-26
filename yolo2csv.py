import csv
import os
import cv2
from tqdm import tqdm

ann_path = '../train/A/'
res_csv = csv.writer(open('train.csv', 'w', newline=''))

for ann in tqdm(os.listdir(ann_path)):
    if '.txt' in ann:
        ann_txt = open(ann_path + ann).readlines()
        w = cv2.imread(ann_path + ann.split('.')[0] + '.jpg').shape[1]
        h = cv2.imread(ann_path + ann.split('.')[0] + '.jpg').shape[0]

        for line in ann_txt:
            l = line.rstrip('\n').split(' ')
            # print(l)
            x1 = (float(l[1]) * w) - (float(l[3]) * w / 2)
            y1 = (float(l[2]) * h) - (float(l[4]) * h / 2)
            x2 = x1 + (float(l[3]) * w)
            y2 = y1 + (float(l[4]) * h)
            res_csv.writerow([ann.split('.')[0], x1, y1, x2, y2, 'ship'])

