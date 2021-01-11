import json
import os
import cv2


with open('./xxx.bbox.json', 'r') as f:
    dic = json.load(f)

res = []

# for key in range(6):
#     res[str(key)] = []
for i, ann in enumerate(dic):
    # print(i)
    dic_out={}
    dic_out['name']=ann['image_id']+'.jpg'
    dic_out['category']=ann['category_id']
    x1=round(ann['bbox'][0],2)
    y1=round(ann['bbox'][1],2)
    x2=round(ann['bbox'][2]+ann['bbox'][0],2)
    y2=round(ann['bbox'][3]+ann['bbox'][1],2)
    #print(x1,y2)
    dic_out['bbox']=[x1,y1,x2,y2]
    dic_out['score']=ann['score']
    res.append(dic_out)
    #print(dic_out)
fp=open('result.json', 'w')
json.dump(res, fp, indent=4, ensure_ascii=False)
