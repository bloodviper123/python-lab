
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author

    def display(self):
        print("Publisher:", self.name)
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        Book.__init__(self, name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        Book.display(self)
        print("Price:", self.price)
        print("Number of Pages:", self.no_of_pages)



n = input("Enter the name of the publisher: ")
t = input("Enter the book title: ")
a = input("Enter the author name: ")
p = float(input("Enter the price: "))
pages = int(input("Enter the number of pages: "))


b = Python(n, t, a, p, pages)


print("\nBook Details")
b.display()