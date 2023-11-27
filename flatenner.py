import fitz  # PyMuPDF

import os

# Get the current directory
current_directory = os.getcwd()

# Loop through all files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".pdf"):
        print("Processing:", filename)

        doc = fitz.open(filename)
        out = fitz.open()  # output PDF

        for page in doc:
            w, h = page.rect.br  # page width / height taken from bottom right point coords
            outpage = out.new_page(width=w, height=h)  # out page has same dimensions
            pix = page.get_pixmap(dpi=150)  # set desired resolution
            outpage.insert_image(page.rect, pixmap=pix)
        out.save("Consulta_"+filename, garbage=3, deflate=True)