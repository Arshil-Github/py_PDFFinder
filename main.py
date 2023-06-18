import PyPDF2
import pickle

#Class Reference for Final references
class reference:
    def __init__(self, pageText, pageNum):
        self.pageText = pageText
        self.pageNum = pageNum

#Converting PDF to Pickle for efficiency------------------------------
# for j in range(7, 17):
    
#     betterj = str(j)

#     if j < 10:
#         betterj = "0" + str(j)
     
#     fileLoc = "Pdfs\lebo1" + str(betterj) + ".pdf"

#     PDF = PyPDF2.PdfFileReader(fileLoc)

#     rfileName = "BookText.pkl"
#     rfileObj = open(rfileName, 'rb')
#     finalArray = pickle.load(rfileObj)
#     rfileObj.close()

#     totalPages = PDF.getNumPages()

#     currentPages = len(finalArray) + 1

#     for i in range(0, totalPages):
#         if i + currentPages == 480:
#             text = "Shame"
#             finalRef = reference(text, i + currentPages)
#             finalArray.append(finalRef)
#             print("Hall of Shame")
#         else:
#             text = PDF.getPage(i).extractText()
#             finalRef = reference(text, i + currentPages)
#             finalArray.append(finalRef)
#             print(finalRef.pageNum)

#     fileName = "BookText.pkl"
#     fileObj = open(fileName, 'wb')
#     pickle.dump(finalArray, fileObj)
#     fileObj.close()

#reading those files---------------------------------------------------
rfileName = "BookText.pkl"
rfileObj = open(rfileName, 'rb')

loadedList = pickle.load(rfileObj)

rfileObj.close();


word = input("Enter your word: ")

for i in range(0, len(loadedList)):
    ptext = loadedList[i].pageText.lower();


    aword = " " + word.lower() + " "
    bword = " " + word.lower() + "."
    cword = " " + word.lower() + ","
    dword = " " + word.lower() + ";"
    eword = " " + word.lower() + ":"
    fword = " " + word.lower() + "-"
    gword = " " + word.lower() + ")"
    hword = "(" + word.lower() + " "
    if aword in ptext or bword in ptext or cword in ptext or dword in ptext or eword in ptext or fword in ptext or gword in ptext or hword in ptext:
        if loadedList[i].pageNum + 1 < 347:
            print("Class 11th Pg - " + str(loadedList[i].pageNum))
        else:
            print("Class 12th Pg - " + str(loadedList[i].pageNum - 346))

# Pickle Storage-----------------------------------------------
# fileName = "test.pkl"
# fileObj = open(fileName, 'wb')
# pickle.dump(finalArray, fileObj)
# fileObj.close()

# word = input("Enter your word: ")

# totalPages = testPDF.getNumPages()

# finalArray = []

# for i in range(3, totalPages):
#     str = testPDF.getPage(i).extractText()
#     if str.find(word) != -1:
#         finalArray.append(i + 1)

# print(finalArray)