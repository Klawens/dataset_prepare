import json, csv


dic = {
    0:'BladderAnastomosis', 1:'PullingTissue', 2:'PullingSeminalVesicle',
    3:'CuttingSeminalVesicle', 4:'CuttingProstate', 5:'CuttingTissue',
    6:'BladderNeckDissection', 7:'PullingProstate', 8:'SuckingBlood',
    9:'SuckingSmoke', 10:'PullingBladderNeck', 11:'PullingVasDeferens',
    12:'UrethraDissection', 13:'ClippingSeminalVesicle', 14:'CuttingMesocolon',
    15:'ClippingBladderNeck', 16:'ClippingVasDeferens', 17:'ClippingTissue',
    18:'CuttingVasDeferens', 19:'CuttingThread', 20:'BaggingProstate',
    21:'MovingDownBladder', 22:'GraspingCatheter', 23:'PassingNeedle'
}

p_res = csv.writer(open('p_val.csv', 'w', newline=''))
r_res = csv.writer(open('r_val.csv', 'w', newline=''))

j1 = json.load(open('phantom_val.json', 'r'))
j2 = json.load(open('real_val.json', 'r'))

for i in j1['annotations']:
    p_res.writerow([i['image_id'], i['bbox'][0], i['bbox'][1], i['bbox'][0]+i['bbox'][2], i['bbox'][1]+i['bbox'][3], dic[i['category_id']]])

for i in j2['annotations']:
    r_res.writerow([i['image_id'], i['bbox'][0], i['bbox'][1], i['bbox'][0]+i['bbox'][2], i['bbox'][1]+i['bbox'][3], dic[i['category_id']]])