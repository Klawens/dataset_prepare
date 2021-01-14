import json
import numpy as np
import pandas as pd
f=open('./xxx.bbox.json','r')
dic=json.load(f)
res={}
PredictionStrings=[]	
image_ids=[]
for i,ann in enumerate(dic):
    image_id=ann['image_id']
    res[image_id]=[]
for i,ann in enumerate(dic):
    image_id=ann['image_id']
    score=ann['score']
    category=ann['category_id']-1
    x1=round(ann['bbox'][0],2)
    y1=round(ann['bbox'][1],2)
    x2=round(ann['bbox'][2]+ann['bbox'][0],2)
    y2=round(ann['bbox'][3]+ann['bbox'][1],2)
    res[image_id].append([category,score,x1,y1,x2,y2])
ct=0
for i,image_id in enumerate(res):
    image_ids.append(image_id)
    tmp= np.array(res[image_id])
    PredictionString=""
    if np.max(tmp[:,1])>0.6:
        ct=ct+1
        for j,ann in enumerate(res[image_id]):
            if j==0:
                PredictionString=PredictionString+"{} {} {} {} {} {}".format(ann[0],ann[1],ann[2],ann[3],ann[4],ann[5])
            else:
                PredictionString=PredictionString+" {} {} {} {} {} {}".format(ann[0],ann[1],ann[2],ann[3],ann[4],ann[5])
        PredictionStrings.append(PredictionString)
    else:
        PredictionStrings.append("14 1 0 0 1 1")
dataframe = pd.DataFrame({'image_id':image_ids,'PredictionString':PredictionStrings})
dataframe.to_csv("image_sample_submission.csv",index=False)           
print(ct)
