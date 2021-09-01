"""
created by Klawens
2021, 8.10
"""
import csv
import os
import xml.dom.minidom as md
from tqdm import tqdm

xmls = 'val/'
res = csv.writer(open('./val.csv', 'w', newline=''))
unique_cat = []

for xml in tqdm(os.listdir(xmls)):
    DOMTree = md.parse(xmls + xml)
    collection = DOMTree.documentElement
    categories = collection.getElementsByTagName('name')
    # boxes = collection.getElementsByTagName('point')  # Change this field to VOC tag
    xmin = collection.getElementsByTagName('xmin')
    ymin = collection.getElementsByTagName('ymin')
    xmax = collection.getElementsByTagName('xmax')
    ymax = collection.getElementsByTagName('ymax')

    category_list = []
    xmin_list = []
    ymin_list = []
    xmax_list = []
    ymax_list = []
    for cat in categories:
        category_list.append(cat.childNodes[0].data)
        if cat.childNodes[0].data not in unique_cat:
            unique_cat.append(cat.childNodes[0].data)
    # for box in boxes:
    #     box_list.append(box.childNodes[0].data.split(','))
    for x_min in xmin:
        xmin_list.append(x_min.childNodes[0].data)
    for y_min in ymin:
        ymin_list.append(y_min.childNodes[0].data)
    for x_max in xmax:
        xmax_list.append(x_max.childNodes[0].data)
    for y_max in ymax:
        ymax_list.append(y_max.childNodes[0].data)

    n = 0
    step = 1  # 1 if is voc format
    for category in category_list:
        # modify this if is voc format
        # if category != 'waterweeds':
        res.writerow([xml.split('.')[0], xmin_list[n], ymin_list[n], xmax_list[n], ymax_list[n], category])
        # res.writerow(
        #     [xml.split('.')[0], box_list[n][0], box_list[n][1], box_list[n + 1][0], box_list[n + 2][1], category])
        n += step
        
print(unique_cat)
