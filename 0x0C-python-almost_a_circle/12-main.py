#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)           # [Rectangle] (1) 1/9 - 10/2
    print(r1)
    r1_dictionary = r1.to_dictionary()
    # {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
    print(r1_dictionary)
    print(type(r1_dictionary))            # dict

    r2 = Rectangle(1, 1)                   # [Rectangle] (2) 0/0 - 1/1
    print(r2)                              # [Rectangle] (2) 0/0 - 1/1
    r2.update(**r1_dictionary)             # [Rectangle] (1) 1/9 - 10/2
    print(r2)
    print(r1)
    u = r2.to_dictionary()
    print(u)
    print(r1 == r2)
