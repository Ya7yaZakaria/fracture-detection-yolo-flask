from pathlib import Path

import cv2
from ultralytics import YOLO


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "deliverables" / "model" / "best.pt"

FRACTURE_CLASS_ID = 0
FRACTURE_THRESHOLD = 0.05
LOCATION_THRESHOLD = 0.50

LOCATION_NAMES = {
    1: "Hand / Wrist Region",
    3: "Hip Region",
    4: "Leg Region",
    5: "Shoulder Region",
}

_model = None


def get_model():
    global _model

    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Trained model was not found at: {MODEL_PATH}"
            )

        _model = YOLO(str(MODEL_PATH))

    return _model


def intersection_over_fracture(fracture_box, region_box):
    fx1, fy1, fx2, fy2 = fracture_box
    rx1, ry1, rx2, ry2 = region_box

    ix1 = max(fx1, rx1)
    iy1 = max(fy1, ry1)
    ix2 = min(fx2, rx2)
    iy2 = min(fy2, ry2)

    intersection_width = max(0, ix2 - ix1)
    intersection_height = max(0, iy2 - iy1)
    intersection_area = intersection_width * intersection_height

    fracture_area = max(1, (fx2 - fx1) * (fy2 - fy1))

    return intersection_area / fracture_area


def detect_fracture(image_path, output_path):
    model = get_model()

    results = model.predict(
        source=str(image_path),
        imgsz=640,
        conf=FRACTURE_THRESHOLD,
        verbose=False,
    )

    result = results[0]
    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError("The uploaded image could not be read.")

    fracture_boxes = []
    region_boxes = []

    if result.boxes is not None:
        for box in result.boxes:
            class_id = int(box.cls.item())
            confidence = float(box.conf.item())
            coordinates = list(
                map(int, box.xyxy[0].cpu().tolist())
            )

            if class_id == FRACTURE_CLASS_ID:
                fracture_boxes.append(
                    {
                        "box": coordinates,
                        "confidence": confidence,
                    }
                )

            elif (
                class_id in LOCATION_NAMES
                and confidence >= LOCATION_THRESHOLD
            ):
                region_boxes.append(
                    {
                        "box": coordinates,
                        "confidence": confidence,
                        "location": LOCATION_NAMES[class_id],
                    }
                )

    fracture_detected = len(fracture_boxes) > 0

    highest_confidence = (
        max(item["confidence"] for item in fracture_boxes)
        if fracture_boxes
        else 0.0
    )

    matched_locations = []

    for fracture in fracture_boxes:
        best_match = None
        best_overlap = 0.0

        for region in region_boxes:
            overlap = intersection_over_fracture(
                fracture["box"],
                region["box"],
            )

            if overlap > best_overlap:
                best_overlap = overlap
                best_match = region

        if best_match is not None and best_overlap >= 0.20:
            matched_locations.append(best_match["location"])

        x1, y1, x2, y2 = fracture["box"]
        confidence = fracture["confidence"]

        label = f"Fracture {confidence * 100:.1f}%"

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            3,
        )

        cv2.putText(
            image,
            label,
            (x1, max(y1 - 10, 25)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )

    if matched_locations:
        location = ", ".join(sorted(set(matched_locations)))
    elif fracture_detected:
        location = "Fracture region highlighted by bounding box"
    else:
        location = "Not applicable"

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not cv2.imwrite(str(output_path), image):
        raise RuntimeError("Failed to save the annotated prediction image.")

    return {
        "fracture_detected": fracture_detected,
        "status": (
            "Fracture Detected"
            if fracture_detected
            else "No Fracture Detected Above Threshold"
        ),
        "confidence": round(highest_confidence * 100, 2),
        "location": location,
        "detection_count": len(fracture_boxes),
        "annotated_image_path": str(output_path),
    }

