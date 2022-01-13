###fitz below is from a library called PyMuPDF and can be accessed and installed via https://github.com/pymupdf/PyMuPDF
import fitz

result = fitz.open()

for pdf in ['file1.pdf', 'file2.pdf', 'file3.pdf']:
    with fitz.open(pdf) as mfile:
        result.insert_pdf(mfile)
    
result.save("result.pdf")
