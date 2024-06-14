from PyPDF2 import PdfReader

# Test basique pour vérifier l'importation
try:
    reader = PdfReader()
    print("PdfReader imported and instantiated successfully.")
except Exception as e:
    print(f"Error: {e}")

pdf_reader = PdfReader('/home/mael/Dokumente/visual-vocabulary-trainer1/src/vocgui/histoire.pdf')

page_content = {}

for indx, pdf_page in enumerate(pdf_reader.pages):
    page_content[indx + 1] = pdf_page.extract_text()

print(page_content)