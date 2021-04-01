import json

f = json.load(open('train.json', 'r'))

for i in f['images']:
    lable = open('trains/'+i['id']+'.txt', 'w')
    for j in f['annotations']:
        if j['image_id'] == i['id']:
            lable.write(
                str(j['category_id']) + ' ' + str((j['bbox'][0]+0.5*j['bbox'][2])/i['width']) + ' ' + str((j['bbox'][1]+0.5*j['bbox'][3])/i['height']) + ' ' + str(j['bbox'][2]/i['width']) + ' ' + str(j['bbox'][3]/i['height']) + '\n'
                )