#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A2 = tuple_a + (0, 0)
    B2 = tuple_b + (0, 0)
    new_tuple = A2[0]+B2[0], A2[1]+B2[1]
    return new_tuple
