# Assignment-1-Python-Assessment

# Objective
Extract text blocks from a PDF document with each paragraph as a separate line and text being in reading order going from first column from top to bottom and then into second column and then third column. Dump the output in an excel file.
The solution should be a general solution that can work on different pages of different PDFs.

# Resources & Hints
* PyMuPDF – PDF Parsing library
* Identify columns by looking at the x coordinates difference
* OpenCV can be used to combine lines using contours

# PDF File
http://www.kepcorp.com/annualreport2018/pdf/keppel-corporation-limited-annual-report-2018.pdf

# Libraries Used
* ##  PyPDF2 
  
  It is a library in Python used to work with PDF files. It can be used for various purposes such as:

  * Merging multiple PDF files into one file.
  * Splitting a single PDF file into multiple files.
  * Extracting text and images from PDF files.
  * Encrypting and decrypting PDF files.
  * Modifying metadata of a PDF file.
  * Rotating and cropping pages in a PDF file.
  * Adding watermarks and annotations to PDF files.

  In short, PyPDF2 can be used to perform various operations on PDF files, making it a versatile tool for working with PDFs in Python.

*  ## Pandas

  Help convert the output text to a dafaframe so it can be converted to an Excel file.
