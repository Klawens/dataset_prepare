import os
import cv2
import csv
import json
import time
import numpy as np


# MMDetection inference result json
with open('./xxx.bbox.json', 'r') as f:
    dic = json.load(f)
res = []
for i, ann in enumerate(dic):
    dic_out={}
    dic_out['name']=ann['image_id']+'.jpg'
    dic_out['category']=ann['category_id']
    x1=round(ann['bbox'][0],2)
    y1=round(ann['bbox'][1],2)
    x2=round(ann['bbox'][2]+ann['bbox'][0],2)
    y2=round(ann['bbox'][3]+ann['bbox'][1],2)
    dic_out['bbox']=[x1,y1,x2,y2]
    dic_out['score']=ann['score']
    res.append(dic_out)
fp=open('result.json', 'w')
json.dump(res, fp, indent=4, ensure_ascii=False)
fp.close()
f.close()

# Generate unique names
print('Generating unique names.....')
with open('result.json', 'r') as f:
    j = json.load(f)
c = open('unique_name.csv', 'w')
csv_f = csv.writer(c)
name = 'xx'
for i in j:
    if i['name'] != name:
        name = i['name']
        csv_f.writerow([os.path.splitext(name)[0]])
c.close()
f.close()
print('Unique names Generated...')
time.sleep(0.5)

# Append Strings
r = csv.reader(open('unique_name.csv', 'r'))
sub_f = csv.writer(open('submit.csv', 'w'))
ff = open('result.json', 'r')
json_f = json.load(ff)
s = ''
k=0
sub_f.writerow(['image_id', 'PredictionString'])
for c in r:
    for i in json_f:
        if i['name'] == c[0] + '.jpg':
            s += str(i['category'] - 1) + ' ' + str(i['score']) + ' ' + str(i['bbox'][0]) + ' ' + str(i['bbox'][1]) + ' ' + str(i['bbox'][2]) + ' ' + str(i['bbox'][3]) + ' '
    sub_f.writerow([c[0], s])
    k+=1
    s = ''
    print('image: NO.%d Done.' % k)
print('Finished\n :D')
