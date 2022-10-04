#Book is the 'Node' object for this AVL tree
#Each Book contains information relevant to the library:
    #Quantity, Name, and Description of the Book
    #Book also contains a link to up to three other Books, for searching tree
class Book:
    name = None
    contents = None
    appearance = None

    #initialization function just initializes name to a placeholder
    #The Node's data will be processed through a .csv file
    #Each row in that csv file holds info about one Book, which are assigned
    def __init__(self, givenRow):
        if(len(givenRow) > 2):
            self.name = givenRow[0]
            self.appearance = givenRow[1]
            self.contents = givenRow[2]
        elif(len(givenRow) > 1):
             self.name = givenRow[0]
             self.contents = givenRow[1]
        elif(len(givenRow) > 0):
             self.name = givenRow[0]
        else:
            name = None
            contents = None
            appearance = None
            
    #prints information about this book
    def descBook(self):
        if(self.name == None):
            print("The book has no known title.")
        else:
            print("The book's title is:", self.name.lstrip('," ').rstrip().rstrip('," '))
        if(self.appearance == None):
            print("The library has no record of this book's appearance, only its presence.")
        else:
            print("The book looks like:", self.appearance.lstrip('," ').rstrip().rstrip('"'))
        if(self.contents == None):
            print("The library has no record of this book's contents. It's possibly cursed.")
        else:
            print("The book's contents include:", self.contents.lstrip('," ').rstrip().rstrip('"'))
        print("")
