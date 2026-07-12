from pathlib import Path

import cv2
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "deliverables" / "model" / "best.pt"

FRACTURE_CLASS_ID = 0
CONFIDENCE_THRESHOLD = 0.25

_model = None


def get_model():
    """Load the trained YOLO model once and reuse it."""
    global _model

    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Trained model was not found at: {MODEL_PATH}"
            )

        _model = YOLO(str(MODEL_PATH))

    return _model


def detect_fracture(image_path, output_path):
    """
    Detect fracture bounding boxes in an uploaded X-ray image.

    Returns:
        Dictionary containing detection status, confidence,
        detection count, and annotated image path.
    """
    model = get_model()

    results = model.predict(
        source=str(image_path),
        imgsz=640,
        conf=CONFIDENCE_THRESHOLD,
        classes=[FRACTURE_CLASS_ID],
        verbose=False,
    )

    result = results[0]
    boxes = result.boxes

    detection_count = 0
    confidences = []

    if boxes is not None and len(boxes) > 0:
        detection_count = len(boxes)
        confidences = boxes.conf.cpu().tolist()

    fracture_detected = detection_count > 0
    highest_confidence = max(confidences) if confidences else 0.0

    annotated_image = result.plot()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not cv2.imwrite(str(output_path), annotated_image):
        raise RuntimeError("Failed to save the annotated prediction image.")

    return {
        "fracture_detected": fracture_detected,
        "status": (
            "Fracture Detected"
            if fracture_detected
            else "No Fracture Detected"
        ),
        "confidence": round(highest_confidence * 100, 2),
        "detection_count": detection_count,
        "annotated_image_path": str(output_path),
    }