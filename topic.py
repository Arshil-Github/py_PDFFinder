import PyPDF2
import pickle


#Converting PDF to Pickle for efficiency------------------------------
fileLoc = "Pdfs/NEET.pdf"

PDF = PyPDF2.PdfFileReader(fileLoc)

finalArray = []

totalPages = PDF.getNumPages()


for i in range(3, totalPages):
    text = PDF.getPage(i).extractText()
    finalRef = text
    finalArray.append(finalRef)
    print(i)

fileName = "PastYear.pkl"
fileObj = open(fileName, 'wb')
pickle.dump(finalArray, fileObj)
fileObj.close()