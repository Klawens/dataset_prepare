from ensemble_boxes import *
import json, os, numpy, cv2


model0 = json.load(open('1.bbox.json', 'r'))
model1 = json.load(open('2.bbox.json', 'r'))

weights = [2, 1]
iou_thr = 0.5
skip_box_thr = 0.0001

n = 0
for img in os.listdir('data/test/'):
    w, h = cv2.imread('data/test/'+img).shape[1], cv2.imread('data/test/'+img).shape[0]
    # print(img.split('.')[0])
    model0_box = []
    model1_box = []
    model0_score = []
    model1_score = []
    model0_label = []
    model1_label = []
    model0_id = []
    model1_id = []
    for img0 in model0:
        # print(img0)
        if img0['image_id'] == int(img.split('.')[0]):
            model0_box.append([img0['bbox'][0]/w, img0['bbox'][1]/h, (img0['bbox'][0]+img0['bbox'][2])/w, (img0['bbox'][1]+img0['bbox'][3])/h])
            model0_score.append(img0['score'])
            model0_label.append(img0['category_id'])
            model0_id.append(img0['image_id'])
    for img1 in model1:
        if img1['image_id'] == int(img.split('.')[0]):  
            model1_box.append([img1['bbox'][0]/w, img1['bbox'][1]/h, (img1['bbox'][0]+img1['bbox'][2])/w, (img1['bbox'][1]+img1['bbox'][3])/h])
            model1_score.append(img1['score'])
            model1_label.append(img1['category_id'])
            model1_id.append(img1['image_id'])

    boxes_list = [model0_box, model1_box]
    scores_list = [model0_score, model1_score]
    labels_list = [model0_label, model1_label]

    boxes, scores, labels = weighted_boxes_fusion(
        boxes_list, scores_list, labels_list, weights=weights, iou_thr=iou_thr, skip_box_thr=skip_box_thr)
    # boxes_list = numpy.array(boxes_list)
    # print(boxes.shape)
    

    ######### Your output format here #########
    # output = open('res/{}.txt'.format(img.split('.')[0]), 'w')
    # n += 1
    # print(str(n) + ': ' + img)
    # boxes = numpy.array(boxes)
    # print(boxes.shape, scores.shape, labels.shape)
    # for j in range(len(boxes)):
    #     output.write('{} {} {} {} {}\n'.format(boxes[j][0]*w, boxes[j][1]*h, boxes[j][2]*w, boxes[j][3]*h, scores[j]))
