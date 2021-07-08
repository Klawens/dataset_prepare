import json
import csv
import os

file = open('../detectors_33.64.json', 'r')
result = csv.writer(open('pseudo.csv', 'w', newline=''))
f = json.load(file)

images = os.listdir('../test_images/')

category_match = {
    1: "pedestrian",
    2: "people",
    3: "bicycle",
    4: "car",
    5: "van",
    6: "truck",
    7: "tricycle",
    8: "awning-tricycle",
    9: "bus",
    10: "motor"
}

for i in f:
    if i['image_id'] + '.jpg' in images:
        # thres
        if i['score'] >= 0.495:
            result.writerow(
                [i['image_id'], i['bbox'][0], i['bbox'][1], i['bbox'][0] + i['bbox'][2], i['bbox'][1] + i['bbox'][3],
                 category_match[i['category_id']]])
