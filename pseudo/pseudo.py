import json
import csv

file = open('xxx.bbox-0.264.json', 'r')
result = csv.writer(open('pseudo.csv', 'w'))
f = json.load(file)
pred = open('pred.csv', 'r')
pred = csv.reader(pred)

abnormal = []

for item in pred:
    if float(item[1]) > 0.08:
        abnormal.append(item[0])

category_match = {
    1: "Aortic enlargement",
    2: "Atelectasis",
    3: "Calcification",
    4: "Cardiomegaly",
    5: "Consolidation",
    6: "ILD",
    7: "Infiltration",
    8: "Lung Opacity",
    9: "Nodule/Mass",
    10: "Other lesion",
    11: "Pleural effusion",
    12: "Pleural thickening",
    13: "Pneumothorax",
    14: "Pulmonary fibrosis",
}

for i in f:
    if i['image_id'] in abnormal:
        # thres 0.5
        # if i['score'] > 0.5:
        #     result.writerow([i['image_id'], i['bbox'][0], i['bbox'][1], i['bbox'][0]+i['bbox'][2], i['bbox'][1]+i['bbox'][3], category_match[i['category_id']]])
        # scheduled thres
        if (i['score'] > 0.5) or ((i['category_id'] != 1 or 4) and i['score'] > 0.4):
            result.writerow([i['image_id'], i['bbox'][0], i['bbox'][1], i['bbox'][0]+i['bbox'][2], i['bbox'][1]+i['bbox'][3], category_match[i['category_id']]])
