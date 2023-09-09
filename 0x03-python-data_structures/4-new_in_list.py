#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None and 0 <= idx < len(my_list):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
