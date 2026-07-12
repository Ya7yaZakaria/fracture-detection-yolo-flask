from pathlib import Path
import shutil

source_dir = Path("deliverables/unseen_predictions")
target_dir = Path("deliverables/unseen_cases")

target_dir.mkdir(parents=True, exist_ok=True)

images = sorted(
    [
        path
        for path in source_dir.iterdir()
        if path.suffix.lower() in {".jpg", ".jpeg", ".png"}
    ]
)

selected_images = images[:10]

for old_file in target_dir.iterdir():
    if old_file.is_file() and old_file.name != ".gitkeep":
        old_file.unlink()

for index, image_path in enumerate(selected_images, start=1):
    new_name = f"unseen_case_{index:02d}{image_path.suffix.lower()}"
    shutil.copy2(image_path, target_dir / new_name)

print(f"Copied {len(selected_images)} unseen prediction images.")
for image_path in sorted(target_dir.glob("unseen_case_*")):
    print(image_path)
