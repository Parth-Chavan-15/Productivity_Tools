# Bulk Certificate Generator & Splitter

A complete, end-to-end workflow to generate hundreds of personalized certificates and automatically split them into individual, properly named `.jpg` files. 

This repository relies on a hybrid approach: using Canva's Bulk Create feature for the visual design and PDF generation, followed by a Python script (`split_cert.py`) to handle the heavy lifting of chopping the master PDF into individual image files.

## 🚀 Prerequisites
*   **Python 3.x** installed on your system.
*   **Canva Pro** (Currently required for the "Bulk Create" tool. *See roadmap below for future free alternatives*).
*   Your participant data in an Excel/CSV file.

## 📦 Step 1: Initial Data Preparation (For Canva)
1. Open your Excel sheet containing the participant names.
2. Ensure the first row contains your event name (e.g., "Invictus"), and the participant names start from the second row. The first row (rather first entry) is for identifying the dataset and does not get included in the certificates generated.
3. **Important Limits:** Canva's Bulk Create tool has a maximum dataset limit of **250 rows**. If you have 500 participants, you must divide your main Excel sheet into two separate files and repeat this process for each.
4. Save the file(s) as **CSV (Comma delimited) (*.csv)**.

## 🎨 Step 2: Canva Bulk Generation
1. Create your certificate design in Canva. **Ensure your document contains only 1 page.**
2. On the left sidebar, go to **Apps** and select **Bulk create**.
3. Choose **Upload CSV** and select your prepared file.
4. Right-click the placeholder text on your certificate design, select **Connect data**, and choose your event name data field. 
5. Click **Continue**, then **Generate**.

> **⚠️ CANVA PAGINATION QUIRK:**
> When generating large datasets, Canva often splits the output into smaller batches (e.g., capping at 80 pages per design file). If you have 200 participants, Canva might generate three separate files instead of one. 
> 
> Download each of these generated files as **PDF Standard**.

## 🗂️ Step 3: Merging PDFs (If Applicable)
If Canva split your certificates into multiple PDF files due to the pagination quirk:
1. Go to a free PDF merger tool (like [iLovePDF](https://www.ilovepdf.com/merge_pdf)).
2. Upload all the separated PDF files in the correct order.
3. Merge and download them as one single **Master PDF**.

## ⚙️ Step 4: Modifying the CSV (For Python)
Before running the script, you must adapt the CSV file so Python can read it properly.
1. Open your original CSV file.
2. **Delete the row containing the event name.**
3. Type the word **Name** in the very first cell (A1) as the column header.
4. Ensure the participant names now start directly from the second row.
5. Save the file (If you encounter character reading errors in Python later, save as CSV UTF-8).

## 🐍 Step 5: Python Setup & Execution
Now we take that Master PDF and split it into individual `.jpg` files named after each participant.

1. **Install Dependencies:**
   Open your terminal and install the required libraries for reading PDFs and images:
   ```bash
   pip install PyMuPDF Pillow
   ```

2. **Configure the Script:**
   Open `split_cert.py` and update the three file paths under the `# --- CONFIGURATION ---` section to match your local machine.

   ```python
   # --- CONFIGURATION ---
   pdf_path = r"C:\path\to\your\Master_Certificates.pdf"  # Your merged PDF
   csv_path = r"C:\path\to\your\Names.csv"                # Your modified CSV file
   output_folder = r"C:\path\to\your\Output_Folder"       # Where the JPGs will go
   ```

3. **Run the Script:**
   Execute the file in your terminal:
   ```bash
   python split_cert.py
   ```
   The script will verify the number of pages matches the number of names in your CSV, and then save every page as a pristine `.jpg` file in your output directory!

## 🗺️ Roadmap / Future Scope
*   **Fully Open-Source Alternative:** Currently, this workflow relies on Canva Pro for the bulk creation step. Future updates will explore completely free alternatives.