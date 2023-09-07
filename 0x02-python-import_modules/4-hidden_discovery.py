#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for i in range(len(dir(hidden_4))):
        if (dir(hidden_4)[i][:2] == "__"):
            continue
        print(dir(hidden_4)[i])
