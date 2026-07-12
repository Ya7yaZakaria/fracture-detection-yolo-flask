# FracAtlas Dataset Description

## Dataset Overview

The FracAtlas dataset is an orthopedic X-ray dataset designed for fracture detection and localization. It contains X-ray images with YOLO-format bounding-box annotations that identify fracture regions and general anatomical regions.

## Dataset Statistics

- Total number of X-ray images: 9,463
- Images containing fracture annotations: 1,707
- Images without fracture annotations: 7,756
- Total fracture bounding-box instances: 2,199
- Image dimensions: 640 × 640 pixels
- Number of classes: 6

## Classes

The dataset contains the following classes:

0. fractured
1. hand
2. hardware
3. hip
4. leg
5. shoulder

The Flask application primarily uses class 0, `fractured`, to determine fracture detection status and draw fracture bounding boxes.

## Annotation Format

Annotations are stored in YOLO TXT format. Each line contains:

class_id x_center y_center width height

All coordinates are normalized relative to the image dimensions.

## Dataset Split

The dataset was divided using a stratified 70/20/10 split:

- Training set: 6,624 images
- Validation set: 1,892 images
- Testing set: 947 images

The test set includes 171 images containing fracture annotations and 218 fracture bounding boxes.

## Strengths

- Large collection of orthopedic X-ray images.
- Includes fracture localization using bounding boxes.
- Contains multiple anatomical regions.
- Suitable for YOLO object-detection training.
- Images are standardized to 640 × 640 pixels.

## Limitations

The dataset is imbalanced. Only approximately 18% of images contain fracture annotations, while approximately 82% do not contain a fracture annotation. The anatomical classes are also unevenly distributed, with leg images represented more frequently than other regions.

The dataset does not provide detailed fracture-location labels such as distal radius, femoral neck, or tibial shaft. Therefore, precise anatomical fracture names cannot be generated reliably. The precise detected area is instead shown visually using the YOLO bounding box.

Images described as non-fracture images are images without a `fractured` annotation according to the provided dataset labels; this does not represent an independent clinical reassessment.
