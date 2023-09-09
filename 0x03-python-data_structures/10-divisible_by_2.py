#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        bool_list = []
        for index in my_list:
            if index % 2 == 0:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
