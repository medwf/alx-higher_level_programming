#!/usr/bin/python3
"""pascal_triange module"""


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


def combinations(n, k):
    a, b, c = fac(n), fac(k), fac(n - k)
    return int(a / (b * c))


def pascal_triangle(n):
    """
    Args:
        n (int): The number pascal triangle
    Return: a list od lists of integers
    """

    # check if n less or equal 0 return empty list
    if n <= 0:
        return []
    # list of lists
    lst = []
    # start loop from 0 to n - 1
    for i in range(n):
        # # i use 11 ** i eash line
        # """
        # for n == 5
        # line 1 = 11 ** 0 = 1
        # line 2 = 11 ** 1 = 11
        # line 3 = 11 ** 2 = 121
        # line 4 = 11 ** 3 = 1331
        # line 5 = 11 ** 4 = 14641
        # """
        # number = 11 ** i
        # # test number is
        # print("number = ", number)
        # # change number to string to take each num from begginng.
        # # casting char to int and make list
        # _l = [int(digit) for digit in str(number)]
        # # test list inside print("inside list = ", _l)
        # lst.append(_l)
        # # test list of list print("all list = ", lst)
        i2 = i
        _l = []
        for k in range(i2 + 1):
            print(combinations(i, k))
            _l.append(combinations(i, k))
        lst.append(_l)

    return lst
