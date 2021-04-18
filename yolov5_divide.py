import os, random, shutil

# random.seed(3)

files = os.listdir('all')
image_list = []
random_list = []
train, val = [], []

for f in files:
    if f.split('.')[1] != 'txt':
        image_list.append(f)
print('image：{}'.format(len(image_list)))
for r in range(60000):
    if len(random_list) == 600:
        break
    k = random.randint(0, 4321)
    if k not in random_list:
        random_list.append(k)
    else:
        r -= 1
for i in range(4322):
    if i in random_list:
        val.append(image_list[i].split('.')[0])
    else:
        train.append(image_list[i].split('.')[0])
print('val: {}, train: {}'.format(len(val), len(train)))

for v in val:
    shutil.copyfile('all/'+v+'.txt', 'val/'+v+'.txt')
    shutil.copyfile('all/'+v+'.png', 'val/'+v+'.png')
    print(v)
for t in train:
    shutil.copyfile('all/'+t+'.txt', 'train/'+t+'.txt')
    shutil.copyfile('all/'+t+'.png', 'train/'+t+'.png')
    print(t)
