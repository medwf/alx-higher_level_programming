#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is not None and 0 <= idx < len(my_list):
        for i in range(len(my_list)):
            if idx == i:
                del my_list[i]
    return my_list
