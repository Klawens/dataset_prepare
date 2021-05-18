import pydicom
import scipy.misc
import os

path = 'dicom_path'
images = os.listdir(path)
#print(images)
for i in images:
    #print(i)
    in_ = path + i
    out = 'jpg_path' + os.path.splitext(i)[0] + '.jpg'
    ds = pydicom.read_file(in_)
    img = ds.pixel_array
    print(img.shape)

    scipy.misc.imsave(out,img)