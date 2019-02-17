from PyPDF2 import PdfFileMerger
import os

os.chdir(str(input(r"Enter directory e.g. C:\Users\ " )))
pdfs = [x for x in os.listdir()]

pdfs.sort()

merger = PdfFileMerger(strict = False)

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
