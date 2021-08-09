"""
created by Klawens
2021, 8.10
"""
import csv
import os
import xml.dom.minidom as md
from tqdm import tqdm

xmls = '../trainData/gt/'
res = csv.writer(open('./train.csv', 'w', newline=''))
unique_cat = []

for xml in tqdm(os.listdir(xmls)):
    DOMTree = md.parse(xmls + xml)
    collection = DOMTree.documentElement
    categories = collection.getElementsByTagName('name')
    boxes = collection.getElementsByTagName('point')  # Change this field to VOC tag

    category_list = []
    box_list = []
    for cat in categories:
        category_list.append(cat.childNodes[0].data)
        if cat.childNodes[0].data not in unique_cat:
            unique_cat.append(cat.childNodes[0].data)
    for box in boxes:
        box_list.append(box.childNodes[0].data.split(','))

    n = 0
    step = 4  # 4 if is voc format
    for category in category_list:
        # modify this if is voc format
        res.writerow([xml.split('.')[0], box_list[0], box_list[1], box_list[2], box_list[3], category])
        # res.writerow(
        #     [xml.split('.')[0], box_list[n][0], box_list[n][1], box_list[n + 1][0], box_list[n + 2][1], category])
        n += step
        
print(unique_cat)
