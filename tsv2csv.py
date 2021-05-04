import csv, os

real_img_path_t = '../MESAD/mesad-real/train/images/'
real_imgs_t = os.listdir(real_img_path_t)
phantom_img_path_t = '../MESAD/mesad-phantom/train/images/'
phantom_imgs_t = os.listdir(phantom_img_path_t)

real_anno_path_t = '../MESAD/mesad-real/train/annotations/'
real_annos_t = os.listdir(real_anno_path_t)
phantom_anno_path_t = '../MESAD/mesad-phantom/train/annotations/'
phantom_annos_t = os.listdir(phantom_anno_path_t)

real_img_path_v = '../MESAD/mesad-real/val/images/'
real_imgs_v = os.listdir(real_img_path_v)
phantom_img_path_v = '../MESAD/mesad-phantom/val/images/'
phantom_imgs_v = os.listdir(phantom_img_path_v)

real_anno_path_v = '../MESAD/mesad-real/val/annotations/'
real_annos_v = os.listdir(real_anno_path_v)
phantom_anno_path_v = '../MESAD/mesad-phantom/val/annotations/'
phantom_annos_v = os.listdir(phantom_anno_path_v)

real_train = csv.writer(open('real_train.csv', 'w', newline=''))
real_val = csv.writer(open('real_val.csv', 'w', newline=''))
phantom_train = csv.writer(open('phantom_train.csv', 'w', newline=''))
phantom_val = csv.writer(open('phantom_val.csv', 'w', newline=''))

for ri in real_imgs_t:
    label = []
    l_0, l_1 = [], []
    for ra in real_annos_t:
        if ri.split('.')[0] == ra.split('.')[0]:
            label.insert(0, ra) if 'labels' in ra else label.insert(1, ra)
    f0 = open(real_anno_path_t + label[0], 'r', newline='')
    f1 = open(real_anno_path_t + label[1], 'r', newline='')
    for i in f0:
        l_0.append(i.rstrip('\n').split('\t'))
    for i in f1:
        l_1.append(i.rstrip('\n').split('\t'))
    for j in range(len(l_0)):
        real_train.writerow([ri.split('.')[0]] + l_1[j] + l_0[j])
    f0.close()
    f1.close()

for ri in real_imgs_v:
    label = []
    l_0, l_1 = [], []
    for ra in real_annos_v:
        if ri.split('.')[0] == ra.split('.')[0]:
            label.insert(0, ra) if 'labels' in ra else label.insert(1, ra)
    f0 = open(real_anno_path_v + label[0], 'r', newline='')
    f1 = open(real_anno_path_v + label[1], 'r', newline='')
    for i in f0:
        l_0.append(i.rstrip('\n').split('\t'))
    for i in f1:
        l_1.append(i.rstrip('\n').split('\t'))
    for j in range(len(l_0)):
        real_val.writerow([ri.split('.')[0]] + l_1[j] + l_0[j])
    f0.close()
    f1.close()

for pi in phantom_imgs_t:
    label = []
    l_0, l_1 = [], []
    for pa in phantom_annos_t:
        if pi.split('.')[0] == pa.split('.')[0]:
            label.insert(0, pa) if 'labels' in pa else label.insert(1, pa)
    f0 = open(phantom_anno_path_t + label[0], 'r', newline='')
    f1 = open(phantom_anno_path_t + label[1], 'r', newline='')
    for i in f0:
        l_0.append(i.rstrip('\n').split('\t'))
    for i in f1:
        l_1.append(i.rstrip('\n').split('\t'))
    for j in range(len(l_0)):
        phantom_train.writerow([pi.split('.')[0]] + l_1[j] + l_0[j])
    f0.close()
    f1.close()

for pi in phantom_imgs_v:
    label = []
    l_0, l_1 = [], []
    for pa in phantom_annos_v:
        if pi.split('.')[0] == pa.split('.')[0]:
            label.insert(0, pa) if 'labels' in pa else label.insert(1, pa)
    f0 = open(phantom_anno_path_v + label[0], 'r', newline='')
    f1 = open(phantom_anno_path_v + label[1], 'r', newline='')
    for i in f0:
        l_0.append(i.rstrip('\n').split('\t'))
    for i in f1:
        l_1.append(i.rstrip('\n').split('\t'))
    for j in range(len(l_0)):
        phantom_val.writerow([pi.split('.')[0]] + l_1[j] + l_0[j])
    f0.close()
    f1.close()
