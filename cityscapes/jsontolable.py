# -*- coding: utf-8 -*-
import json
import cv2
import numpy as np
import os
import shutil
import argparse
 
#labellist=['flat':0,'human':1,'vehicle':2,'construction':3,'objec':4,'nature':5,'sky':6]
def cvt_one(json_path, img_path, save_path, label_color):
    # load img and json
    data = json.load(open(json_path,encoding='gbk'))
    img = cv2.imread(img_path)
 
    # get background data
    img_h = data['imgHeight']
    img_w = data['imgWidth']
    color_bg = (0, 0, 0)
    points_bg = [(0, 0), (0, img_h), (img_w, img_h), (img_w, 0)]
    img = cv2.fillPoly(img, [np.array(points_bg)], color_bg)
 
    # draw roi
    for i in range(len(data['objects'])):
        name = data['objects'][i]['label']
        #print(name)
        points = data['objects'][i]['polygon']
      
        #data['shapes'][i]['fill_color'] = label_color[name]  # 修改json文件中的填充颜色为我们设定的颜色
        if label_color:
             #print(label_color[name])
             img = cv2.fillPoly(img, [np.array(points, dtype=int)], label_color[name])
        
        # else:
             #img = cv2.fillPoly(img, [np.array(points, dtype=int)], (color[0], color[1], color[2]))
    img_cvt_cat = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(save_path, img_cvt_cat)
 
 
if __name__ == '__main__':
    save_dir ='../data/2'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
 
    file_dir = '../data/datasetv2/datasetv2'
    files = os.listdir(file_dir)
    img_files = list(filter(lambda x: '.png' in x, files))
    
    label_color = { #设定label染色情况
        'fence':(255,255,255),'falt':(0,0,0),'road':(255,255,255),'void':(255,255,255),'flat':(0,0,0),
        'human':(1,1,1),'vehicle':(2,2,2),'construction':(3,3,3),'constrution':(3,3,3),'object':(4,4,4),
        'obiect':(4,4,4),'objec':(4,4,4),'nature':(5,5,5),'sky':(6,6,6)
    }
    save_img='../data/2'
    if not os.path.exists(save_img):
        os.makedirs(save_img)
    for i in range(len(img_files)):
        img_path = file_dir + '/' + img_files[i]
        
        
        shutil.copy(img_path, save_img + '/' + img_files[i])
        json_path = img_path.replace('.png', '.json')
        #print(json_path)
        save_path = save_dir + '/' + img_files[i]
        print(i)
        cvt_one(json_path, img_path, save_path, label_color)
  