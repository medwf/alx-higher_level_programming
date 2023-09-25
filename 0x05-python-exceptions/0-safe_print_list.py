#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    if x <= 0:
        return idx
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            idx += 1
        print()
        return x
    except:
        print()
        return idx
