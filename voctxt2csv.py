import cv2
import os
import csv

file_list = 'DarkFace_Train_2021/label/'
file_name = os.listdir(file_list)
output = open('data.csv', 'w')
output = csv.writer(output)

for name in file_name:
    with open(file_list + name, 'r') as f:
        print(name.split('.')[0])
        txt = f.readlines()[1:]
        for ann in txt:
            output.writerow([name.split('.')[0], ann.split()[0], ann.split()[1], ann.split()[2], ann.split()[3], 'face'])
