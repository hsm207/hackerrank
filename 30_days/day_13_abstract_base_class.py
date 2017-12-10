from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print('Title: {}\nAuthor: {}\nPrice: {}'.format(self.title, self.author, self.price))


x = MyBook('The Alchemist', 'Paulo Coelho', 248)
x.display()