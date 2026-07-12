from pathlib import Path
from uuid import uuid4

from flask import Blueprint, current_app, flash, render_template, request
from werkzeug.utils import secure_filename

from app.inference import detect_fracture


main = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        uploaded_file = request.files.get("xray_image")

        if uploaded_file is None or uploaded_file.filename == "":
            flash("Please select an X-ray image.", "danger")
            return render_template("index.html")

        if not allowed_file(uploaded_file.filename):
            flash(
                "Unsupported file format. Please upload JPG, JPEG, or PNG.",
                "danger",
            )
            return render_template("index.html")

        extension = secure_filename(uploaded_file.filename).rsplit(".", 1)[1].lower()
        unique_name = f"{uuid4().hex}.{extension}"

        upload_folder = Path(current_app.static_folder) / "uploads"
        result_folder = Path(current_app.static_folder) / "results"

        upload_folder.mkdir(parents=True, exist_ok=True)
        result_folder.mkdir(parents=True, exist_ok=True)

        upload_path = upload_folder / unique_name
        result_name = f"result_{unique_name}"
        result_path = result_folder / result_name

        uploaded_file.save(upload_path)

        try:
            prediction = detect_fracture(upload_path, result_path)
        except Exception as error:
            current_app.logger.exception("Fracture detection failed.")
            flash(f"Prediction failed: {error}", "danger")
            return render_template("index.html")

        return render_template(
            "index.html",
            prediction=prediction,
            original_image=f"uploads/{unique_name}",
            result_image=f"results/{result_name}",
        )

    return render_template("index.html")