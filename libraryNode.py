import csv

#Book is the 'Node' object for this AVL tree
#Each Book contains information relevant to the library:
    #Quantity, Name, and Description of the Book
    #Book also contains a link to up to three other Books, for searching tree
class Book:
    name = None
    quantity = None
    contents = None
    appearance = None
    left = None
    right = None
    parent = None

    #initialization function just initializes name to a placeholder
    #The Node's data will be processed through a .csv file
    def __init__(self):
        self.name = 'Undefined'

    #Reads a specified row in a .csv file and places its data into this object
    def SetBook(self):
        with open("List of Useless books for nosy adventurers.csv") as inFile:
            csvFileReader = csv.reader(inFile)
            for row in csvFileReader:
                if(row != None):
                    print(row[0])

    #prints information about this book
    def descBook(self):
        if(self.quantity == None or self.quantity < 1):
            print("The library has no available copies of the book titled:", self.name)
        else:
            print("The library has", self.quantity, "copies of", self.name, "available.")
        if(self.appearance == None):
            print("The library has no record of this book's appearance, only its presence.")
        else:
            print("The book looks like:", self.appearance)
        if(self.contents == None):
            print("The library has no record of this book's contents. It's possibly cursed.")
        else:
            print("The book's contents include: ", self.contents, "\n\n")
