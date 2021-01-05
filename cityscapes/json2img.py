import json
import os
import numpy as np
import  cv2
names=os.listdir('../data/json/')

cls_lab = {
    'flat': 0,
    'human': 1,
    'vehicle': 2,
    'construction': 3,
    'object': 4,
    'nature': 5,
    'sky': 6
}
for i,name in enumerate(names):
    print(i)
    #if i==1:
        #break
    f=open('../data/json/{}'.format(name),'r')
    dic=json.load(f)
    #print(len(dic['objects']))
    height=dic['imgHeight']
    width=dic['imgWidth']
    img= np.ones([height, width], dtype = np.uint8)*255 
    #img=print(img)
    print(height,width)
    for j,ann in enumerate(dic['objects']):
        label_index=cls_lab[ann['label']]
        ploy=ann['polygon']
        b = np.array([ploy])
        cv2.fillPoly(img, b, label_index) 
    cv2.imwrite('../data/2/{}.png'.format(name[:-5]),img)
        #print(img)
        #print(np.unique(img))
       # print(b.shape)
       # print(type(ploy))
       # print(label_index)
       # print(ann)
'''    
im = np.zeros([240, 320], dtype = np.uint8) 
cv2.polylines(im, a, 1, 255) 
cv2.fillPoly(im, b, 255) 
'''