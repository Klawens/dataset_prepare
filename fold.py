import os, csv, json, random

random.seed(67)

f_val_1 = open('fold_1/fold_1_val.csv', 'w', newline = "")
f_val_2 = open('fold_2/fold_2_val.csv', 'w', newline = "")
f_val_3 = open('fold_3/fold_3_val.csv', 'w', newline = "")
f_val_4 = open('fold_4/fold_4_val.csv', 'w', newline = "")
res_val_1 = csv.writer(f_val_1)
res_val_2 = csv.writer(f_val_2)
res_val_3 = csv.writer(f_val_3)
res_val_4 = csv.writer(f_val_4)

img_root = 'train/'
fold_0_train = json.load(open('fold_0/train.json', 'r'))

image_id = []
for i in fold_0_train['images']:
    image_id.append(i['id'])
print(len(image_id))

random_list_1 = []
for r in range(999999):
    if len(random_list_1) == 1200:
        break
    k = random.randint(0, 4800)
    if k not in random_list_1:
        random_list_1.append(k)
random_list_2 = []
for r in range(999999):
    if len(random_list_2) == 1200:
        break
    k = random.randint(0, 4800)
    if (k not in random_list_2) and (k not in random_list_1):
        random_list_2.append(k)
random_list_3 = []
for r in range(999999):
    if len(random_list_3) == 1200:
        break
    k = random.randint(0, 4800)
    if (k not in random_list_2) and (k not in random_list_1) and (k not in random_list_3):
        random_list_3.append(k)
random_list_4 = []
for r in range(999999):
    if len(random_list_4) == 1200:
        break
    k = random.randint(0, 4800)
    if (k not in random_list_2) and (k not in random_list_1) and (k not in random_list_3) and (k not in random_list_4):
        random_list_4.append(k)

print(len(random_list_1))
print(len(random_list_2))
print(len(random_list_3))
print(len(random_list_4))

for k in random_list_1:
    for j in fold_0_train['annotations']:
        if j['image_id'] == k:
            res_val_1.writerow([k, j['bbox'][0], j['bbox'][1], j['bbox'][0]+j['bbox'][2], j['bbox'][1]+j['bbox'][3], 'face'])
    print(k)
for k in random_list_2:
    for j in fold_0_train['annotations']:
        if j['image_id'] == k:
            res_val_2.writerow([k, j['bbox'][0], j['bbox'][1], j['bbox'][0]+j['bbox'][2], j['bbox'][1]+j['bbox'][3], 'face'])
    print(k)
for k in random_list_3:
    for j in fold_0_train['annotations']:
        if j['image_id'] == k:
            res_val_3.writerow([k, j['bbox'][0], j['bbox'][1], j['bbox'][0]+j['bbox'][2], j['bbox'][1]+j['bbox'][3], 'face'])
    print(k)
for k in random_list_4:
    for j in fold_0_train['annotations']:
        if j['image_id'] == k:
            res_val_4.writerow([k, j['bbox'][0], j['bbox'][1], j['bbox'][0]+j['bbox'][2], j['bbox'][1]+j['bbox'][3], 'face'])
    print(k)
