#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    else:
        num = my_list[0]
        for idx in my_list:
            if num < idx:
                num = idx
        return num
    return
