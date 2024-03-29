#!/usr/bin/env python
#
# Created by carlosjimz on 24/11/2018 11:29
#
##############################################################
import operator
from functools import reduce
from typing import Dict, List


def args(*nums):
    return sum(map(lambda v: v, nums))


def kwargs(**data):
    return ', '.join("{!s}={!r}".format(key, val) for (key, val) in data.items())


def args_kwargs(*nums, **data):
    return sum(map(lambda v: v, nums)), ', '.join("{!s}={!r}".format(key, val) for (key, val) in data.items())


if __name__ == '__main__':
    print("**********ARGS*********")
    print(args(1))
    print(args(1, 2, 3))
    print(args(1, 2, 3, 4, 5, 6, 7))

    print("\n********KWARGS*********")
    print(kwargs(Firstname="Peter"))
    print(kwargs(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890))
    print(kwargs(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
                 Country="Wakanda", Age=25, Phone=9876543210, Gender="Male"))

    print("\n********ARGS AND KWARGS*********")
    print(args_kwargs(1, 2, 3, 4, 5, 6, 7, Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
                      Country="Wakanda", Age=25, Phone=9876543210, Gender="Male"))
