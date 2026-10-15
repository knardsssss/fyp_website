"""Package the HTML/CSS website with its PHP WordPress wrapper."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
page = (root / "index.html").read_text(encoding="utf-8")
content = page.split("<body>", 1)[1].rsplit("</body>", 1)[0]
output = root / "wordpress" / "fyp-project-page.zip"
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    archive.writestr("fyp-project-page/content.html", content)
    archive.write(root / "styles.css", "fyp-project-page/styles.css")
    archive.write(root / "wordpress" / "fyp-project-page.php", "fyp-project-page/fyp-project-page.php")
print(f"Created {output}")
