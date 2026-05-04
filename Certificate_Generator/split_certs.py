import fitz  # PyMuPDF
from PIL import Image
import os
import csv

# --- CONFIGURATION ---
pdf_path = r"C:\Users\parth\Downloads\Invictus.pdf"  # add your PDF file
csv_path = r"C:\Users\parth\Downloads\Invictus.csv"                        # add your CSV file with names
output_folder = r"C:\Users\parth\Downloads\Invictus_Certificates_Output"                         # folder to save JPGs

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read names from CSV
names = []
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming CSV column header is 'Name'
        names.append(row['Name'])

# Open PDF
doc = fitz.open(pdf_path)

# Check if number of pages matches number of names
if len(doc) != len(names):
    print("Warning: Number of PDF pages and number of names in CSV do not match!")

# Loop through pages and save as JPG with names
for page_number in range(len(doc)):
    page = doc[page_number]
    
    # Convert page to image
    pix = page.get_pixmap()
    
    # Convert pixmap to PIL image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Get the name for this page, remove invalid filename characters
    person_name = names[page_number]
    person_name = "".join(c for c in person_name if c.isalnum() or c in (" ", "_", "-")).strip()
    
    # Set output file path
    output_path = os.path.join(output_folder, f"{person_name}.jpg")
    
    # Save image
    img.save(output_path, "JPEG")
    print(f"Saved: {output_path}")

print(f"\nAll {len(doc)} certificates converted to JPGs in:\n{output_folder}")
