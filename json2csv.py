import json
import csv
import os


json_f = json.load(open('/4TB-HDD1/lsc/data/tianchi/round1/train/train_annos.json', 'r'))
csv_f = open('train.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_f)
# print(json_f[0])

for i in json_f:
    filename = os.path.splitext(i['name'])[0]
    height = i['image_height']
    width = i['image_width']
    if i['category'] == 0:
        category = '背景'
    elif i['category'] == 1:
        category = "边异常"
    elif i['category'] == 2:
        category = "角异常"
    elif i['category'] == 3:
        category = "白色点瑕疵"
    elif i['category'] == 4:
        category = "浅色块瑕疵"
    elif i['category'] == 5:
        category = "深色点块瑕疵"
    else:
        category = "光圈瑕疵"
    xmin = i['bbox'][0]
    ymin = i['bbox'][1]
    xmax = i['bbox'][2]
    ymax = i['bbox'][3]

    csv_writer.writerow([filename, xmin, ymin, xmax, ymax, category])
    print(filename, xmin, ymin, xmax, ymax, category)

csv_f.close()




