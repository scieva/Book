class Book:
    def __init__(self, author=[], title="", publisher="", published=""):
        # initialising the class its self with the needed attributes
        self.authors = author
        self.title = title
        self.publisher = publisher
        self.publicationyear = published

    def __str__(self):
        # a simple method to printing the object attributes as a string
        a = ', '.join(map(str, self.authors))
        return "%s - %s, %s, %s" % (a, self.title, self.publisher, self.publicationyear)


class Library:
    def __init__(self, books=[]):
        # initialising the class its self so we can keep as many books as we wish
        self.books = books

    def ReadBooks(self, inputString):
        inputString = inputString.split('\n') # transforming the string to an array, for easier processing
        for line in inputString:
            if line == "Book:":
                # checking if the current element from the array of lines is "Book: ", if it is, that means that we are
                # entering a new book, so we need an empty object
                b = Book()
                b.authors = []
            elif line == "":
                # checking if the current element from the array of lines is "", if it is, that means that we finished
                # entering the previous book, so we add it to the list of books that are saved
                self.books.append(b)
            else:
                # if the current element from the array of lines doesn't fulfill any of the previous condition, that means
                # we started entering specific data for the book
                # firstly, we split the line (element) in two subelemets, where the first one is the specific category
                # of the publishing information of the book, and the second one is the data of category itself
                y = line.split(": ")
                if y[0] == "Author":
                    b.authors.append(y[1])
                elif y[0] == "Title":
                    b.title = y[1]
                elif y[0] == "Publisher":
                    b.publisher = y[1]
                elif y[0] == "Published":
                    b.publicationyear = y[1]
        return self.books

    def FindBooks(self, searchString):
        # list for the book that the method returns
        b = []
        # firstly, transforming the search string to all lower characters and removing all the "*" for easier processing
        searchString = searchString.lower()
        ss = searchString.replace('*', '')
        # secondly, if there is more then one filter, we split the string
        searchString = ss.split(' ')
        # I added a flag so if not one book is found containing the wanted string the method prints that information
        flag = False
        for book in self.books:
            # as per what was given, I made three types of filters
            # one that has only one condition that has to be satisfied
            if searchString.__len__() == 1 and searchString[0] in book.__str__():
                flag = True
                b.append(book)
            # one that has two conditions and both have to be satisfied
            elif searchString.__len__() > 1 and searchString[0] in book.__str__().lower() and searchString[1] == "&" and \
                    searchString[2] in book.__str__().lower():
                flag = True
                b.append(book)
            # and one that has two conditions but only one has to be satisfied
            elif searchString.__len__() > 1 and searchString[1] == "or" and \
                    (searchString[0] in book.__str__().lower() or searchString[2] in book.__str__().lower()):
                flag = True
                b.append(book)
        if not flag:
            print("None of the books contain " + ss)
        return b


# it's named "inputString", and not "input" so it doesn't shadow built-in name "input"
inputString = """Book:
Author: Brian Jensen
Title: Texts from Denmark
Publisher: Gyldendal
Published: 2001

Book:
Author: Peter Jensen
Author: Hans Andersen
Title: Stories from abroad
Publisher: Borgen
Published: 2012
"""

lib = Library()
lib.ReadBooks(inputString)
# since FindBooks returns a list, we save that, and after go through it so it can print the books we found
foundbooks = lib.FindBooks("*20* & *peter*")
for i in foundbooks:
    print(i.__str__())

# other examles I tried out

# a = """Book:
# Author: Andre Aciman
# Title: Find me
# Publisher: Farrar, Straus and Giroux
# Published: 2019
# """
# lib.ReadBooks(a)
# foundbooks = lib.FindBooks("*2013* & *Adam*")
# foundbooks = lib.FindBooks("*2001* or *Andre*")
# foundbooks = lib.FindBooks("*DRE*")
# for i in foundbooks:
#     print(i.__str__())
