#!/usr/bin/python3
"""pascal_triange module"""


def fac(n):
    """
    a funcyion calculate factorial of n
    Argv:
        n (int): the number that calculat factorial
    Return: fac(n)
    """
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


def combinations(n, k):
    """
    a function calculat combinations for (n, k)
    Argv:
        n (int) : items
        k (int) : itens
    using this method C(n,k)= n! / k!(n-k)!.
    Return: int of C(n, k)
    """
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
        i2 = i
        _l = []
        for k in range(i2 + 1):
            # test print(combinations(i, k))
            _l.append(combinations(i, k))
        lst.append(_l)

    return lst
