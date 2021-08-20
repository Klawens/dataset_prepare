import random
import cv2
import json

annotation = json.load(open('../train.json', 'r'))

for anno in annotation['annotations']:
    for img in annotation['images']:
        if str(img['id']) == str(anno['image_id']):
            image = img['file_name']
    img = cv2.imread('../train/JPEGImages/{}'.format(image))
    w, h = img.shape[1], img.shape[0]

    if anno['category_id'] == 4:
        x1, y1 = anno['bbox'][0], anno['bbox'][1]
        x2, y2 = anno['bbox'][0] + anno['bbox'][2], anno['bbox'][1] + anno['bbox'][3]
        crop = img[y1:y2, x1:x2, :]
        cv2.imwrite('pothole/{}_{}_{}_{}.jpg'.format(image.split('.')[0], w, anno['category_id'], random.randint(0, 101)),
                    crop)