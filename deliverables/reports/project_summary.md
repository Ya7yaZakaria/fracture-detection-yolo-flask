# Fracture Detection Using YOLO and Flask

## Project Objective

This project develops an automatic fracture detection system using YOLO object detection and a Flask web application.

The system accepts an orthopedic X-ray image, detects possible fracture regions, draws bounding boxes, and displays the prediction confidence.

## Dataset

Dataset: FracAtlas

Total images: 9,463

Image size: 640 × 640 pixels

Dataset split:

- Training: 6,624 images
- Validation: 1,892 images
- Testing: 947 images

The dataset contains six classes:

- fractured
- hand
- hardware
- hip
- leg
- shoulder

The Flask application uses class 0, `fractured`, as the main fracture detection result.

## Model

Model architecture: YOLO11n

Training epochs: 100

Image size: 640 × 640

Batch size: 16

Hardware: NVIDIA Tesla T4 GPU

## Deliverables

- Trained YOLO model
- Training results
- Test evaluation results
- Prediction images
- Flask web application
- Project report