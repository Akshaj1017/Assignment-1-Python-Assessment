import PyPDF2
import pandas as pd

# Open the PDF file
File = PyPDF2.PdfFileReader(open("keppel-corporation-limited-annual-report-2018.pdf", "rb"))

#Page number Entered by user
Page_No = int(input("Enter the page number: "))

# Get the specified page
Page_Number = File.getPage(Page_No)

# Extract the text from the Specified page
Text = Page_Number.extractText()

# Split the text into different columns
New_Columns = Text.split("\n")

# Write the columns created to an Excel file

df = pd.DataFrame(New_Columns)
df.to_excel("output.xlsx", index=False, header=False)
