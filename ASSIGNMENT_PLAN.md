# Assignment II — Detailed Implementation Plan

## Project Title

**Flask-Based Web Application for Automatic Fracture Detection Using YOLO**

## Submission Deadline

**14 July 2026 — 10:59 PM**

---

## 1. Project Objective

The project will build a complete computer-aided fracture detection system that:

1. Uses the FracAtlas orthopedic X-ray dataset.
2. Prepares the dataset in YOLO object-detection format.
3. Trains a YOLO model to localize fracture regions using bounding boxes.
4. Evaluates the trained model on unseen test images.
5. Integrates the trained model into a Flask web application.
6. Allows users to upload JPG, JPEG, or PNG X-ray images.
7. Displays the original image, annotated result, detection status, and confidence score.
8. Produces documentation, screenshots, metrics, and a final 5–8 page report.

---

## 2. Final Deliverables

The final submission package should contain:

- Flask project source code.
- Trained YOLO model: `best.pt`.
- Dataset preparation documentation.
- Dataset description page.
- YOLO training notebook.
- Training screenshots.
- Training curves.
- Validation and test results.
- Precision, recall, and F1-score.
- Results for at least 10 unseen X-ray images.
- Flask application screenshots.
- Performance evaluation report.
- Final report of 5–8 pages.
- Optional demonstration video.
- README with setup and run instructions.

---

## 3. Recommended Technical Stack

- Python 3.10 or 3.11
- Ultralytics YOLO
- PyTorch
- Flask
- OpenCV
- Pillow
- NumPy
- pandas
- scikit-learn
- Matplotlib
- Bootstrap 5
- Kaggle Notebook for training
- Git and GitHub for version control

---

## 4. Project Architecture

```text
fracture_detection_assignment/
│
├── README.md
├── ASSIGNMENT_PLAN.md
├── CHECKLIST.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── dataset_description.md
│   ├── evaluation_report.md
│   ├── final_report_outline.md
│   └── screenshots_guide.md
│
├── notebooks/
│   └── fracture_yolo_training.ipynb
│
├── scripts/
│   ├── explore_dataset.py
│   ├── prepare_dataset.py
│   ├── evaluate_model.py
│   └── generate_unseen_cases.py
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── inference.py
│   ├── config.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── upload.html
│   │   └── result.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── uploads/
│       └── results/
│
├── models/
│   └── best.pt
│
├── dataset/
│   ├── data.yaml
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── labels/
│       ├── train/
│       ├── val/
│       └── test/
│
├── reports/
│   ├── figures/
│   └── unseen_cases/
│
└── tests/
    ├── test_upload.py
    └── test_inference.py
```

---

## 5. Phase-by-Phase Plan

# Phase 1 — Project Initialization

## Goals

- Create the repository.
- Create the project folder structure.
- Create a Python virtual environment.
- Install dependencies.
- Add `.gitignore`.
- Add README and assignment plan.

## Tasks

1. Create the root project folder.
2. Initialize Git.
3. Create and activate the virtual environment.
4. Install Flask, Ultralytics, OpenCV, Pillow, NumPy, pandas, scikit-learn, and Matplotlib.
5. Freeze dependencies into `requirements.txt`.
6. Create the full folder structure.
7. Make the first commit.

## Output

- Clean repository.
- Working Python environment.
- Organized folder structure.

---

# Phase 2 — Dataset Exploration

## Assignment Weight

**10 marks**

## Goals

Prepare a one-page description of the FracAtlas dataset.

## Required Data to Collect

- Total number of X-ray images.
- Number of fracture images.
- Number of non-fracture images.
- Number of classes.
- Class names.
- Image dimensions.
- Annotation format.
- Number of bounding boxes.
- Whether negative images contain empty annotation files.
- Distribution of fracture and non-fracture images.

## Technical Tasks

1. Inspect the downloaded Kaggle dataset structure.
2. Identify image folders.
3. Identify annotation files.
4. Confirm whether annotations are YOLO, COCO, Pascal VOC, CSV, or segmentation masks.
5. Count all images.
6. Count all labeled fracture images.
7. Count images with no fractures.
8. Calculate minimum, maximum, median, and most common image dimensions.
9. Visualize at least 6 sample images with bounding boxes.
10. Save the findings to `docs/dataset_description.md`.

## Important Rule

The exact counts should be calculated from the downloaded Kaggle copy rather than copied blindly from an article because Kaggle mirrors may differ in organization.

## Output

- One-page dataset description.
- Dataset statistics table.
- Sample annotated images.

---

# Phase 3 — Dataset Conversion and Preparation

## Assignment Weight

**10 marks**

## Target Structure

```text
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

## Split Ratios

- Training: 70%
- Validation: 20%
- Testing: 10%

## Technical Tasks

1. Confirm the annotation format.
2. Convert annotations to YOLO format when needed.
3. Validate every bounding box.
4. Normalize coordinates to values between 0 and 1.
5. Remove or report corrupted images.
6. Pair every image with its corresponding label.
7. Create empty `.txt` label files for valid negative images.
8. Use a fixed random seed: `42`.
9. Prefer stratified splitting where possible.
10. Prevent data leakage.
11. Copy files into train, val, and test folders.
12. Generate `dataset/data.yaml`.
13. Print final split counts.
14. Produce sample visual validation after conversion.

## YOLO Label Format

Each object is stored on one line:

```text
class_id x_center y_center width height
```

All coordinates must be normalized relative to image width and height.

## Data Leakage Checks

- No duplicate image should appear in more than one split.
- Images from the same patient or study should remain in one split when patient identifiers are available.
- File hashes may be used to detect exact duplicates.

## Output

- YOLO-ready dataset.
- `data.yaml`.
- Split summary.
- Annotation validation report.

---

# Phase 4 — YOLO Model Training

## Assignment Weight

**20 marks**

## Required Training Parameters

- Image size: 640 × 640
- Epochs: 100
- Batch size: 16
- Output model: `best.pt`

## Recommended Baseline

Use a lightweight pretrained YOLO detector such as YOLO11n for the first reproducible run.

## Training Tasks

1. Install Ultralytics in Kaggle.
2. Check GPU availability.
3. Load the pretrained YOLO model.
4. Start training using the required parameters.
5. Set a fixed random seed.
6. Save results to a named experiment folder.
7. Save `best.pt` and `last.pt`.
8. Record training duration.
9. Capture screenshots of:
   - GPU environment.
   - Training command.
   - Epoch progress.
   - Final metrics.
10. Export:
   - Loss curves.
   - Precision–recall curve.
   - F1 curve.
   - Confusion matrix.
   - Validation batch predictions.

## Baseline Training Command

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data="/kaggle/working/dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    seed=42,
    project="/kaggle/working/runs",
    name="fracture_detection"
)
```

## Output

- `best.pt`.
- Training screenshots.
- Loss curves.
- Validation results.
- Training configuration.

---

# Phase 5 — Model Evaluation

## Assignment Weight

**10 marks**

## Required Metrics

- Precision.
- Recall.
- F1-score.

## Recommended Additional Metrics

- mAP@50.
- mAP@50–95.
- Number of false positives.
- Number of false negatives.
- Detection confidence distribution.

## Technical Tasks

1. Load `best.pt`.
2. Evaluate only on the test split.
3. Record precision and recall.
4. Calculate F1-score.
5. Record mAP values.
6. Save confusion matrix.
7. Review at least:
   - 3 true positives.
   - 3 true negatives.
   - 3 false positives.
   - 3 false negatives.
8. Discuss model strengths.
9. Discuss model weaknesses.
10. Explain the effect of subtle fractures, image quality, projection, and dataset imbalance.

## F1 Formula

```text
F1 = 2 × Precision × Recall / (Precision + Recall)
```

## Output

- `docs/evaluation_report.md`.
- Metrics table.
- Error analysis.
- Strengths and limitations discussion.

---

# Phase 6 — Flask Web Application

## Assignment Weight

**25 marks**

## Functional Pages

### Home Page

Must contain:

- Project title.
- Short clinical description.
- System purpose.
- Upload button.
- Educational disclaimer.

### Upload Page

Must allow:

- JPG.
- JPEG.
- PNG.
- File browsing.
- File validation.
- Submission to the prediction route.

### Results Page

Must display:

- Original X-ray image.
- Annotated X-ray image.
- Detection status.
- Maximum confidence score.
- Number of detected regions.
- Optional list of all detections.
- Clinical disclaimer.
- Button to analyze another image.

## Flask Components

### `app/config.py`

Responsibilities:

- Upload folder path.
- Result folder path.
- Allowed extensions.
- Maximum upload size.
- Model path.
- Confidence threshold.

### `app/inference.py`

Responsibilities:

- Load YOLO once.
- Run prediction.
- Read bounding boxes.
- Read confidence values.
- Save annotated image.
- Return structured results.

### `app/routes.py`

Responsibilities:

- Home route.
- Upload route.
- Prediction route.
- Result rendering.
- Validation errors.

### Security and Validation

- Use `secure_filename`.
- Restrict extensions.
- Verify file content.
- Set maximum upload size.
- Generate unique filenames.
- Never execute uploaded content.
- Avoid exposing local file paths.
- Handle corrupted images gracefully.

## Detection Logic

- If at least one fracture box is above the confidence threshold:
  - Status: `Fracture Detected`.
  - Display maximum confidence.
  - Display number of detected regions.
- If no valid boxes are found:
  - Status: `No Fracture Detected`.
  - Explain that no detection exceeded the selected threshold.

## Important Clinical Limitation

The model should not automatically claim an anatomical diagnosis such as “distal radius fracture” unless the dataset contains anatomical classes or a separate anatomical classifier is added.

## Output

- Functional Flask application.
- Original and annotated images.
- Confidence score.
- Detection status.
- Screenshots of all pages.

---

# Phase 7 — Ten Unseen Test Cases

## Goals

Produce results for at least 10 X-rays not used for model training.

## Tasks

1. Select 10 images only from the test split.
2. Include fracture and non-fracture cases when available.
3. Run the model using the same confidence threshold.
4. Save original and annotated images.
5. Create a CSV summary with:
   - Image filename.
   - Ground truth.
   - Predicted status.
   - Maximum confidence.
   - Number of detections.
   - Outcome category.
6. Include representative successes and failures.
7. Do not cherry-pick only perfect cases.

## Output

- 10 original images.
- 10 annotated images.
- Summary CSV.
- Screenshots for report inclusion.

---

# Phase 8 — Documentation and Final Report

## Required Length

**5–8 pages**

## Recommended Report Structure

### 1. Introduction

- Clinical importance of fracture detection.
- Role of AI in radiology and orthopedics.
- Why object detection is suitable.
- Purpose of the project.

### 2. Dataset

- FracAtlas overview.
- Image count.
- Fracture count.
- Annotation format.
- Class structure.
- Image dimensions.
- Dataset limitations.

### 3. Methodology

- Dataset preprocessing.
- YOLO annotation conversion.
- Train/validation/test split.
- Data leakage prevention.
- Model selection.
- Training configuration.

### 4. System Architecture

- Training pipeline.
- Inference pipeline.
- Flask architecture.
- Upload and result workflow.
- Model loading strategy.

### 5. Results

- Precision.
- Recall.
- F1-score.
- mAP.
- Training curves.
- Confusion matrix.
- Ten unseen cases.

### 6. Discussion

- Strengths.
- Weaknesses.
- False positives.
- False negatives.
- Effect of image quality.
- Clinical meaning of confidence scores.

### 7. Clinical Significance and Safety

- Computer-aided detection role.
- Human oversight.
- Dataset bias.
- Generalizability.
- Privacy and security.
- Not for standalone diagnosis.

### 8. Conclusion and Future Work

- Project summary.
- Improvements.
- Larger multicenter datasets.
- Anatomical classification.
- External validation.
- Deployment possibilities.

---

# Phase 9 — Testing and Quality Assurance

## Application Tests

- Home page loads.
- Upload page loads.
- Valid JPG upload succeeds.
- Valid PNG upload succeeds.
- Invalid extension is rejected.
- Corrupted image is rejected.
- Oversized file is rejected.
- Model file missing gives a controlled error.
- Result page displays both images.
- No-fracture result is handled correctly.
- Multiple detections are displayed correctly.

## Model Validation Checks

- `best.pt` loads correctly.
- Inference works on CPU.
- Inference works on GPU when available.
- Confidence values are between 0 and 1.
- Saved annotated image exists.
- No test image was used in training.

## Final Clean-Run Test

Test the project in a fresh environment:

1. Clone repository.
2. Create virtual environment.
3. Install `requirements.txt`.
4. Add `best.pt`.
5. Run Flask.
6. Upload an image.
7. Confirm result generation.

---

# Phase 10 — Submission Packaging

## Final Package

```text
submission/
├── source_code/
├── best.pt
├── dataset_documentation.pdf
├── training_results/
├── flask_screenshots/
├── unseen_cases/
├── evaluation_report.pdf
├── final_report.pdf
├── README.md
└── optional_demo_video.mp4
```

## Final Verification

- All required deliverables are present.
- No private dataset credentials are included.
- No unnecessary large training cache files are included.
- `best.pt` opens successfully.
- README instructions are correct.
- Report metrics match notebook outputs.
- Screenshots are readable.
- The application runs from a clean installation.
