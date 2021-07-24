import os, csv


f = open('test.csv', 'w', newline='')
images = os.listdir('/4TB-HDD1/lsc/data/kaggle/xray_det/test_jpg/')
csv_writer = csv.writer(f)

for i in images:
    # print(i)
    name = os.path.splitext(i)[0]
    csv_writer.writerow([name, 1, 1, 1, 1, "ILD"])
    print(name)

f.close()