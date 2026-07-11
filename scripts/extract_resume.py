from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
pdf_path = ROOT / "tmp_resume.pdf"
out_path = ROOT / "memory-bank" / "resume_extracted.txt"

reader = PdfReader(pdf_path)
parts = []
for index, page in enumerate(reader.pages, start=1):
    parts.append(f"=== PAGE {index} ===")
    parts.append(page.extract_text() or "")

out_path.write_text("\n".join(parts), encoding="utf-8")
print(f"Saved {len(parts)} blocks to {out_path}")
