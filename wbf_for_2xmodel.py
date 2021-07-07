from weighted_boxes_fusion.ensemble_boxes import *
import json, os, numpy, cv2, time


model0 = json.load(open('inference_res/retinanet_val_nms.json', 'r'))
model1 = json.load(open('inference_res/faster_val_nms.json', 'r'))

final_boxes, final_scores, final_labels, img_all = [], [], [], []

weights = [1, 2]
iou_thr = 0.5
skip_box_thr = 0.0001

n = 0
for img in os.listdir('val2017/'):
    w, h = cv2.imread('val2017/'+img).shape[1], cv2.imread('val2017/'+img).shape[0]
    # print(img.split('.')[0])
    model0_box, model1_box = [], []
    model0_score, model1_score = [], []
    model0_label, model1_label = [], []
    model0_id, model1_id = [], []
    
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
    
    n += 1
    print(str(n) + ': ' + img)

####################### Your Code Here. ###########################

    final_boxes.append(boxes)
    final_scores.append(scores)
    final_labels.append(labels)
    img_all.append(img.split('.')[0])
    


res = []
for i in range(len(final_boxes)):
    w, h = cv2.imread('val2017/'+img_all[i]+'.jpg').shape[1], cv2.imread('val2017/'+img_all[i]+'.jpg').shape[0]
    print(i)
    for l in range(len(final_boxes[i])):
        temp = {}
        temp['image_id'] = int(img_all[i])
        temp['bbox'] = [final_boxes[i][l][0]*w, final_boxes[i][l][1]*h, (final_boxes[i][l][2]-final_boxes[i][l][0])*w, (final_boxes[i][l][3]-final_boxes[i][l][1])*h]
        temp['score'] = float(final_scores[i][l])
        temp['category_id'] = int(final_labels[i][l])
        res.append(temp)
    print(temp)

print(res)
json.dump(res, open('wbf_res.json', 'w'), indent=4)
