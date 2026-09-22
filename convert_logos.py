import fitz  # PyMuPDF
import sys
import os

def convert_pdf_to_png(pdf_path, output_path):
    print(f"Converting {pdf_path} to {output_path}...")
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)  # Load first page
    pix = page.get_pixmap(dpi=300)
    pix.save(output_path)
    print(f"Saved {output_path}")

base_dir = r"C:\Users\Veerashaiva mart\.gemini\antigravity\brain\d4389f88-0d40-4691-8c7d-ddc6f5f859f5"
assets_dir = r"c:\Users\Veerashaiva mart\OneDrive\Desktop\Veerashaiva_mart_site\src\assets"

files_to_convert = {
    "media__1786208318408.pdf": "blinker_logo.png",
    "media__1786207954309.pdf": "niranthara_logo.png",
    "media__1786207954615.pdf": "coastal_king_logo.png"
}

for pdf_name, png_name in files_to_convert.items():
    pdf_path = os.path.join(base_dir, pdf_name)
    png_path = os.path.join(assets_dir, png_name)
    if os.path.exists(pdf_path):
        convert_pdf_to_png(pdf_path, png_path)
    else:
        print(f"File not found: {pdf_path}")
