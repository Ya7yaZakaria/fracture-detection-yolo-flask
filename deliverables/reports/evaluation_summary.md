# Test Evaluation Summary

## Test Dataset

The trained model was evaluated on an independent test set containing 947 images.

The test set included:

- 171 images containing fracture annotations
- 218 fracture bounding-box instances

## Overall Test Results

- Precision: 0.873
- Recall: 0.896
- mAP50: 0.900
- mAP50-95: 0.627

## Fracture-Class Results

- Precision: 0.586
- Recall: 0.487
- mAP50: 0.480
- mAP50-95: 0.210

## Interpretation

The model achieved strong overall performance across anatomical-region classes.

The fracture class achieved moderate precision and recall. The model can localize some fracture regions correctly, but it may miss a proportion of fractures.

Therefore, the model should be considered an educational decision-support prototype and not a replacement for clinical diagnosis.

## Inference Speed

Average inference speed:

- Preprocessing: 1.2 ms per image
- Inference: 4.0 ms per image
- Postprocessing: 0.9 ms per image