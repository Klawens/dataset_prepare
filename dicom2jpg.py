import pydicom
import scipy.misc
import os

path = '/4TB-HDD1/lsc/data/kaggle/xray_det/test/'
images = os.listdir(path)
#print(images)
for i in images:
    #print(i)
    in_ = path + i
    out = '/4TB-HDD1/lsc/data/kaggle/xray_det/test_jpg/' + os.path.splitext(i)[0] + '.jpg'
    ds = pydicom.read_file(in_)
    img = ds.pixel_array
    print(img.shape)

    scipy.misc.imsave(out,img)