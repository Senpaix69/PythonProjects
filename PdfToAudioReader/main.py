
import pyttsx3
import PyPDF2

file = open("anyPdfFile.path", mode="rb")
pdf_reader = PyPDF2.PdfFileReader(file, strict=False)
pages = pdf_reader.getPage(3)

text = pages.extractText()

milo = pyttsx3.init()
milo.say(text)
milo.runAndWait()
