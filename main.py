import PyPDF2
import os

pdf_files = []  # creating an empty list for files
path = "COMMUNICATION SYSTEM SIR NOTES"


for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        if filename != 'merged.pdf':
            pdf_files.append(filename)

print(pdf_files)
pdf_files.sort()

print(pdf_files)

pdfMerger = PyPDF2.PdfMerger()

for filename in pdf_files:
    file = open(f"{path}/{filename}", 'rb')
    pdfReader = PyPDF2.PdfReader(file)
    pdfMerger.append(pdfReader)

file.close()
pdfMerger.write('merged.pdf')
