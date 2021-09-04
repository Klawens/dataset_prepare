import json
import csv

classname_to_id = {
    0: "phone", 1: "pad", 2: "laptop", 3: "wallet", 4: "packsack"
}

anno = json.load(open('../car_data2/train/annotations.json', 'r'))
csv_res = csv.writer(open('train.csv', 'w', newline=''))

for i in anno['annotations']:
    fn = ''
    for j in anno['images']:
        if j['id'] == i['image_id']:
            fn = j['file_name']

    csv_res.writerow(
        [fn.split('.')[0], i['bbox'][0], i['bbox'][1], i['bbox'][0] + i['bbox'][2], i['bbox'][1] + i['bbox'][3],
         classname_to_id[i['category_id']]])
