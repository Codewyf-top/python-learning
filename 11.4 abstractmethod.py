# -*- coding: utf-8 -*-
"""
@Time ： 22/12/2020 21:09
@Auth ： Codewyf
@File ：11.4 abstractmethod.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
from abc import ABCMeta, abstractmethod

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self):
        pass

class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

document = Document()
document.set_title('Harry Potter')
print(document.get_title())

entity = Entity()
"""
抽象类是一种特殊的类，它生下来就是作为父类存在的，一旦对象化就会报错。
同样，抽象函数定义在抽象类之中，子类必须重写该函数才能使用。相应的抽象函数，
则是使用装饰器 @abstractmethod 来表示。
"""