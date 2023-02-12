import PyPDF2
import pandas as pd

# Open the PDF file
File = PyPDF2.PdfFileReader(open("keppel-corporation-limited-annual-report-2018.pdf", "rb"))

# Getting the specified page(here its page 12)
Page_Number = File.getPage(11)

# Extract the text from the Specified page
Text = Page_Number.extractText()

# Split the text into different columns
New_Columns = Text.split("\n")

# Write the columns created to an Excel file

df = pd.DataFrame(New_Columns)
df.to_excel("output.xlsx", index=False, header=False)
