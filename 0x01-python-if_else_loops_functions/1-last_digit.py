#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check if number positive or negetive and calc last digit
if number >= 0:
    last_d = number % 10
else:
    num = number * -1
    last_d = (num % 10) * -1

# do process print output
if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
