import os
from PIL import Image


files = os.listdir('/4TB-HDD1/lsc/data/kaggle/xray_det/test/')
txt = open('/4TB-HDD1/lsc/data/kaggle/xray_det/test.txt', 'w')
# print(os.path.splitext(files[0])[0])
for f in files:
    # txt.write(os.path.splitext(f)[0] + '\n')
    txt.write(f + '\n')
txt.close()

images = open('/4TB-HDD1/lsc/data/kaggle/xray_det/test.txt', 'r').readlines()
xmls = '/4TB-HDD1/lsc/data/kaggle/xray_det/test_xml/'

for img in images:
    im = Image.open('/4TB-HDD1/lsc/data/kaggle/xray_det/test/' + img.replace('\n', ''))
    width, height = im.size

    # write in xml file
    xml_file = open((xmls + os.path.splitext(img)[0] + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + str(img) + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>1</depth>\n')
    xml_file.write('    </size>\n')
 
    # write the region of image on xml file
    xml_file.write('    <object>\n')
    xml_file.write('        <name>' + 'no' + '</name>\n')
    xml_file.write('        <pose>Unspecified</pose>\n')
    xml_file.write('        <truncated>0</truncated>\n')
    xml_file.write('        <difficult>0</difficult>\n')
    xml_file.write('        <bndbox>\n')
    xml_file.write('            <xmin>' + '0' + '</xmin>\n')
    xml_file.write('            <ymin>' + '0' + '</ymin>\n')
    xml_file.write('            <xmax>' + '0' + '</xmax>\n')
    xml_file.write('            <ymax>' + '0' + '</ymax>\n')
    xml_file.write('        </bndbox>\n')
    xml_file.write('    </object>\n')
 
    xml_file.write('</annotation>')

