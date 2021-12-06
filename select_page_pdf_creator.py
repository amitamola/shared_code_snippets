'''
If you have some .pdf file, but only need a few pages out of the whole and 
you know exactly the page numbers that you want to remove or alternatively keep.
Here's the code to help you do that.

Credit for this code - https://stackoverflow.com/a/39574231/2126357
'''

#Do install the library if not available in the environment you are working on
#!pip install PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

pages_to_keep = [2, 4] # Remember that the page numbers would starts from 0. So Page number 1 will become 0 here.
infile = PdfFileReader('filename.pdf', 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open('Output.pdf', 'wb') as f:
    output.write(f)
