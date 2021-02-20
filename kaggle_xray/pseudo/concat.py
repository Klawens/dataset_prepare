import csv

f1 = open('train.csv', 'r')
f2 = open('pseudo.csv', 'r')
f = open('train_pseudo.csv', 'w')
f1 = csv.reader(f1)
f2 = csv.reader(f2)
f = csv.writer(f)

concat = []
for i in f1:
    concat.append(i)
for i in f2:
    concat.append(i)

f.writerows(concat)
