import csv, os

w, h = 640, 400

seq = 0

res = csv.writer(open('seq{}.csv'.format(seq), 'w', newline=''))

anno_list = os.listdir('seq{}'.format(seq))
for anno in anno_list:
    for line in open('seq{}/'.format(seq) + anno, 'r'):
        line = line.split(' ')
        x1 = (float(line[1])*w) - (float(line[3])*w/2)
        y1 = (float(line[2])*h) - (float(line[4])*h/2)
        x2 = x1 + (float(line[3])*w)
        y2 = y1 + (float(line[4])*h)
        print([str(anno.split('.')[0]), x1, y1, x2, y2, 'person'])
        res.writerow([str(anno.split('.')[0]) + '_', x1, y1, x2, y2, 'person'])