import os
import csv
from shutil import copyfile

f = open('pseudo.csv', 'r')
f = csv.reader(f)

ann = []
for i in f:
    ann.append(i[0])

n = 0
img = os.listdir("../train2017/test2017/")
for j in img:
    if j.split('.')[0] in ann:
        # os.remove("../train2017/test2017/"+j)
        copyfile("../train2017/test2017/"+j, "../train_pseudo/"+j)
        n += 1
        print(n)
