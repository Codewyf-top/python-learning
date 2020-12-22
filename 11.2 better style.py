# -*- coding: utf-8 -*-
"""
@Time ： 22/12/2020 18:22
@Auth ： Codewyf
@File ：11.2 better style.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
"""
如何在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构造？
如果一个函数不涉及到访问修改这个类的属性，而放到类外面有点不恰当，怎么做才能更优雅呢？
既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？
"""

class Document():

    WELCOME_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('Init function  called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')

print('The context of the empty book is: {}'.format(empty_book.get_context_length()))
print(empty_book.get_welcome('Indeed nothing'))