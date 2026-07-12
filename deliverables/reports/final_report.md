# Automatic Fracture Detection Using YOLO and Flask

## 1. Introduction

Fractures are among the most common findings in orthopedic X-ray imaging. Early and accurate detection is important because missed fractures may delay treatment and increase the risk of complications.

This project develops an educational artificial intelligence system for automatic fracture detection using YOLO object detection and a Flask web application. The system allows users to upload orthopedic X-ray images, detects possible fracture regions, draws bounding boxes, and displays confidence scores and detection status.

The project includes dataset exploration, dataset preparation, YOLO model training, model evaluation, Flask web development, and testing on unseen X-ray images.

## 2. Project Objectives

The main objectives were to:

- Understand YOLO object detection.
- Explore and prepare the FracAtlas dataset.
- Divide the dataset into training, validation, and testing sets.
- Train a YOLO model for 100 epochs.
- Evaluate the trained model using precision, recall, F1-score, and mAP.
- Develop a Flask web application.
- Allow users to upload JPG, JPEG, and PNG X-ray images.
- Display fracture bounding boxes and confidence scores.
- Present detection status and general location information.
- Test the system on unseen X-ray images.

## 3. Dataset Exploration

The FracAtlas dataset was used in this project. It contains orthopedic X-ray images with YOLO-compatible annotations for fractures and anatomical regions.

### Dataset Statistics

- Total X-ray images: 9,463
- Images containing fracture annotations: 1,707
- Images without fracture annotations: 7,756
- Fracture bounding-box instances: 2,199
- Image dimensions: 640 x 640 pixels
- Number of classes: 6

### Classes

The dataset contains the following classes:

0. fractured
1. hand
2. hardware
3. hip
4. leg
5. shoulder

The main class used by the Flask application is class 0, fractured.

### Annotation Format

The annotations are stored in YOLO TXT format. Each line contains:

    class_id x_center y_center width height

The coordinates are normalized according to image width and height.

### Dataset Strengths

The dataset includes a large number of orthopedic X-ray images, fracture bounding boxes, and several anatomical regions. It is suitable for training YOLO object-detection models.

### Dataset Limitations

The dataset is imbalanced. Approximately 18% of the images contain fracture annotations, while approximately 82% do not contain fracture annotations.

The anatomical classes are also unevenly distributed, with leg images represented more frequently than hip, shoulder, and hand images.

The dataset does not include detailed anatomical fracture labels such as distal radius, femoral neck, or tibial shaft. Therefore, precise anatomical fracture names cannot be predicted reliably.

## 4. Dataset Preparation

The dataset was reorganized into the standard YOLO directory structure:

    dataset/
        images/
            train/
            val/
            test/
        labels/
            train/
            val/
            test/

The dataset was split using a stratified 70/20/10 approach:

- Training set: 6,624 images
- Validation set: 1,892 images
- Testing set: 947 images

The stratified split preserved approximately the same fracture-image ratio in each subset.

The testing set included:

- 171 images containing fracture annotations
- 218 fracture bounding-box instances

## 5. YOLO Model Training

The YOLO11n architecture was selected because it is lightweight, fast, and suitable for educational deployment in a Flask web application.

### Training Parameters

- Model: YOLO11n
- Image size: 640 x 640 pixels
- Epochs: 100
- Batch size: 16
- Hardware: NVIDIA Tesla T4 GPU
- Best trained checkpoint: deliverables/model/best.pt

The model was trained using the training set and evaluated during training using the validation set.

Training outputs included:

- Training and validation loss curves
- Precision curve
- Recall curve
- F1-confidence curve
- Precision-recall curve
- Confusion matrix
- Validation prediction images
- best.pt
- last.pt

## 6. Model Evaluation

The trained model was evaluated using the independent test set containing 947 images.

### Overall Test Results

- Precision: 0.873
- Recall: 0.896
- F1-Score: 0.884
- mAP50: 0.900
- mAP50-95: 0.627

These results indicate strong overall performance across all six classes.

### Fracture-Class Results

- Precision: 0.586
- Recall: 0.487
- F1-Score: 0.532
- mAP50: 0.480
- mAP50-95: 0.210

The fracture class performed less strongly than the anatomical-region classes.

The fracture recall of 0.487 means that the model missed a proportion of fracture annotations. The moderate precision also indicates that some detected fracture boxes may be false-positive predictions.

### Strengths

- Strong overall precision and recall.
- Fast inference.
- Ability to localize possible fracture regions using bounding boxes.
- Suitable for integration into a Flask web application.
- Good performance for common anatomical-region classes.

### Weaknesses

- Lower performance for the fractured class.
- Dataset imbalance between fracture and non-fracture images.
- Imbalance among anatomical classes.
- Some fractures may be missed.
- Lower confidence thresholds may increase false positives.
- General anatomical location prediction is less reliable than bounding-box localization.

## 7. Flask Web Application

A Flask web application was developed to provide a simple interface for fracture detection.

### Functional Features

The application allows users to:

- Open the home page.
- Browse for an X-ray image.
- Upload JPG, JPEG, or PNG files.
- Run YOLO inference.
- Display the original image.
- Display the annotated image.
- View fracture bounding boxes.
- View confidence scores.
- View the detection status.
- View a general anatomical location when sufficiently reliable.

### Detection Output

When a fracture is detected, the application displays:

- Detection Result
- Fracture Detected
- Confidence percentage
- General location or bounding-box location message
- Original X-ray
- Annotated X-ray

When no fracture prediction exceeds the selected threshold, the application displays:

- Detection Result
- No Fracture Detected Above Threshold

The phrase "Above Threshold" was used because a low-confidence fracture prediction may still exist below the application threshold.

### Location Reporting

The assignment provides "Distal Radius" as an example. However, the dataset does not contain detailed fracture-site classes.

Therefore, the application reports only general regions such as:

- Hand / Wrist Region
- Hip Region
- Leg Region
- Shoulder Region

When the region is not reliable, the application displays:

    Fracture region highlighted by bounding box

This prevents the system from presenting unsupported anatomical detail.

## 8. Unseen X-Ray Testing

The model was tested on at least ten unseen X-ray images.

The prediction results were saved in:

    deliverables/unseen_cases/

The cases demonstrate:

- Fracture bounding boxes
- Confidence scores
- Different anatomical regions
- Variation in model performance

A contact sheet was generated to display all ten cases together for rapid review.

The unseen-case results show that the model can detect and localize some fractures successfully, but may miss some obvious fractures because of the fracture class's moderate recall.

## 9. Clinical Interpretation

The model should be treated as an educational decision-support prototype.

A positive prediction may guide the user's attention to a suspected fracture region, but the bounding box does not confirm a final diagnosis.

A negative prediction does not exclude a fracture, particularly because the fracture-class recall was 0.487.

The system must not replace:

- Radiologist interpretation
- Orthopedic evaluation
- Clinical history
- Physical examination
- Additional imaging

## 10. Future Improvements

Future improvements may include:

- Training a fracture-only YOLO model.
- Oversampling fracture-containing images.
- Applying stronger fracture-focused augmentation.
- Reducing the number of negative training images.
- Training a larger model such as YOLO11s.
- Improving annotation quality.
- Adding more detailed fracture-location labels.
- Training separate models for hand, hip, leg, and shoulder X-rays.
- Performing external validation on a different dataset.
- Adding threshold controls to the Flask interface.
- Adding downloadable prediction reports.

## 11. Conclusion

This project successfully developed a complete AI-powered fracture detection workflow using YOLO and Flask.

The project included dataset exploration, data preparation, model training, test evaluation, Flask application development, and unseen-image testing.

The model achieved strong overall performance, with an overall precision of 0.873, recall of 0.896, and F1-score of 0.884.

However, the fracture class achieved lower performance, with a precision of 0.586, recall of 0.487, and F1-score of 0.532.

The final system can detect possible fracture regions, draw bounding boxes, display confidence scores, and provide a user-friendly web interface.

The system is appropriate as an educational AI prototype but should not be used as a replacement for professional clinical diagnosis.

## Clinical Disclaimer

This project is for educational and research purposes only. It is not a certified medical device and must not be used as the sole basis for diagnosis or treatment.
