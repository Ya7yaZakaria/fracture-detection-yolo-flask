from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    SECRET_KEY = "change-this-in-production"
    MODEL_PATH = BASE_DIR / "models" / "best.pt"
    UPLOAD_FOLDER = BASE_DIR / "app" / "static" / "uploads"
    RESULT_FOLDER = BASE_DIR / "app" / "static" / "results"
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    CONFIDENCE_THRESHOLD = 0.25
