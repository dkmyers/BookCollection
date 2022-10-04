import libraryNode
import csv
import random
#libraryObject is the object which stores and interfaces with the csv file storing these books
class libraryObject:
    #lib is a list of all Book objects created when initialized
    lib = []
    count = 0
    #when initialized, open and process csv file
    def __init__(self):
        with open("List of Useless books for nosy adventurers.csv") as inFile:
            self.listLib = list(inFile)
            for i in self.listLib:
                newBook = libraryNode.Book(self.processCSVLine(i))
                self.lib.append(newBook)
    #takes a line from the library's csv file
    #and separates it into three values
    def processCSVLine(self, givenLine):
        #split the string at an iterator
        #after examining the csv file, this would be: ,"
            #Comma and quotation marks separate cells in csv files
        self.splitLine = givenLine.split(',"')
        return self.splitLine

    def printTitles(self):
        for iterator in self.lib:
            iterator.descBook()
            
    #prints the description of a random book in lib[]
    def getRandomBook(self):
        random.seed()
        self.lib[random.randint(0,len(self.lib)-1)].descBook()
        
test = libraryObject()
for i in range(0, 200, 1):
    test.getRandomBook()
