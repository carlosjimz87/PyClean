#!/usr/bin/env python
#
# Created by carlosjimz on 23/11/2018 17:11
#
##############################################################

from abc import ABCMeta, abstractmethod


# Interface
class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


# # Base
# class Shape(object):
#
#     def area(self): pass
#
#     def perimeter(self): pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

        super(Rectangle, self).__init__()

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return self.width*2 + self.height*2


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        super(Square, self).__init__(side, side)

    def area(self):
        return 2*super(Square, self).area()


s = Shape()
r = Rectangle(5, 6)
print(type(r))
print(r.area())
print(r.perimeter())

sq = Square(5)
print(type(sq))
print(sq.area())
print(sq.perimeter())

