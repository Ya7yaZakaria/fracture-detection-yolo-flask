from pathlib import Path
from PIL import Image, ImageDraw

source = Path("deliverables/unseen_cases")
files = sorted(source.glob("unseen_case_*.jpg"))

thumb_width = 320
thumb_height = 320
label_height = 35
columns = 2
rows = (len(files) + columns - 1) // columns

sheet = Image.new(
    "RGB",
    (columns * thumb_width, rows * (thumb_height + label_height)),
    "white",
)

draw = ImageDraw.Draw(sheet)

for index, file_path in enumerate(files):
    image = Image.open(file_path).convert("RGB")
    image.thumbnail((thumb_width - 10, thumb_height - 10))

    column = index % columns
    row = index // columns

    x = column * thumb_width + (thumb_width - image.width) // 2
    y = row * (thumb_height + label_height) + 5

    sheet.paste(image, (x, y))

    draw.text(
        (column * thumb_width + 10, y + thumb_height),
        file_path.name,
        fill="black",
    )

output = source / "unseen_cases_contact_sheet.jpg"
sheet.save(output, quality=95)

print(f"Created: {output}")
