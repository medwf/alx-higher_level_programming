#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        new_list = my_list.copy()
        for i in range(0, len(my_list)):
            if i == idx:
                new_list[i] = element
            else:
                new_list[i] = my_list[i]
    return new_list
