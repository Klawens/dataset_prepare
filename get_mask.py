import os
import numpy as np
from pycocotools.coco import COCO
from pycocotools import mask as maskUtils
import cv2
import random, json

# Set the paths to the COCO dataset
annFile = '../annos/val_new.json'
imageDir = '../val/'

# Initialize the COCO instance
coco = COCO(annFile)
annos = json.load(open(annFile, 'r'))['annotations']

# Get a random image ID from the dataset
image_ids = coco.getImgIds()
for image_id in image_ids:
    image_path = os.path.join(imageDir, image_id + '.jpg')
    image = cv2.imread(image_path)

    # Iterate through the annotations
    for annotation in annos:
        # Get the segmentation mask
        segmentation = annotation['segmentation']

        # Create a binary mask from the segmentation
        mask = maskUtils.decode(segmentation)

        # Apply the mask to the image
        masked_image = cv2.bitwise_and(image, image, mask=mask)

        # Save the result image
        result_path = os.path.join('mask/', '{}_mask_{}.jpg'.format(image_id, random.randint(0, 1000)))
        cv2.imwrite(result_path, masked_image)

        print("Result mask image saved at:", result_path)
