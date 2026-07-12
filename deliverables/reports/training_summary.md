# Training Summary

## Training Configuration

- Model: YOLO11n
- Epochs: 100
- Batch size: 16
- Image size: 640 × 640
- Optimizer: Automatically selected by Ultralytics
- Device: NVIDIA Tesla T4 GPU
- Random seed: 42

## Training Duration

The model completed 100 epochs in approximately 2.693 hours.

## Validation Results

Overall validation metrics:

- Precision: 0.913
- Recall: 0.887
- mAP50: 0.911
- mAP50-95: 0.618

Fracture-class validation metrics:

- Precision: 0.761
- Recall: 0.483
- mAP50: 0.607
- mAP50-95: 0.267

## Saved Models

- `best.pt`: Best-performing model checkpoint
- `last.pt`: Final training checkpoint