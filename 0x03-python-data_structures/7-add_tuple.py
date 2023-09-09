#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) >= len(list_b):
        for i in range(len(list_b)):
            list_a[i] += list_b[i]
        new_tuple = tuple(list_a)
    else:
        for i in range(len(list_a)):
            list_b[i] += list_a[i]
        new_tuple = tuple(list_b)
    return new_tuple
