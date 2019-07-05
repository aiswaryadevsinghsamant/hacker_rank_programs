from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    @abstractmethod
    def display(self):
        pass

#Write MyBook class


class MyBook(Book):
    def __init__(self, b_title, b_author, b_price):
        self.price = b_price
        super().__init__(b_title, b_author)

    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
