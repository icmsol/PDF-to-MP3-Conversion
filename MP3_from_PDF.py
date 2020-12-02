import PyPDF2
from gtts import gTTS

## Insert the path and title of the PDF you want to convert to MP3 below where it says "Book.pdf"
pdfFileObj = open("Book.pdf", "rb")

## This is not necesarily used in the app, but I left here in case I want for the tool to just read to me rather than saving as a PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

## Code to change pages and iterate through the entire book.
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()
print(mytext)
pdfFileObj.close()


## This part of the code inputs the to an MP3 by the name you select down the place of "Book" below
tts = gTTS(text=mytext, lang='en')
tts.save("Book.mp3")
