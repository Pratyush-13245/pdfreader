import pyttsx3
import PyPDF2

book = open('ds-c.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)

speaker=pyttsx3.init()
for num in range(26,738):
    page=pdfreader.getPage(25)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()