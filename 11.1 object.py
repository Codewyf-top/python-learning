# -*- coding: utf-8 -*-
"""
@Time ： 22/12/2020 18:05
@Auth ： Codewyf
@File ：11.1 object.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
class Document():
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context # __开头的属性是私有属性 私有属性不能被打印

    def get_context_lenght(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '...Forever Do not believe any thing is capable of thinking independently ...')

print('the title is: {}'.format(harry_potter_book.title))
print('the author is: {}'.format(harry_potter_book.author))
print('the length of context: {}'.format(harry_potter_book.get_context_lenght()))

harry_potter_book.intercept_context(10)
print('get intercept_context(10)')
print('the new length of context is: {}'.format(harry_potter_book.get_context_lenght()))
