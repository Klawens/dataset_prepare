import csv

test = open('test.csv', 'r')
submit = open('submit.csv', 'r')

tester = csv.reader(test)
submiter = csv.reader(submit)
s = []
for t in submiter:
    #print(t[0])
    s.append(t[0])

#print(s)
for j in tester:
    #print(j[0])
    if j[0] not in s:
        print(j[0])
