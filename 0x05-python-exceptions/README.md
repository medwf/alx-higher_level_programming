# 0x05. Python - Exceptions

## about:

    - Why Python programming is awesome
    - What’s the difference between errors and exceptions
    - What are exceptions and how to use them
    - When do we need to use exceptions
    - How to correctly handle an exception
    - What’s the purpose of catching exceptions
    - How to raise a builtin exception
    - When do we need to implement a clean-up action after an exception

## Task mandatory:

0. Safe list printing : Write a function that prints x elements of a list.
1. Write a function that prints an integer with "{:d}".format().
2. Write a function that prints the first x elements of a list and only integers.
3. Write a function that divides 2 integers and prints the result.
4. Write a function that divides element by element 2 lists.
5. Write a function that raises a type exception.
6. Write a function that raises a name exception with a message.

## Task advanced

100. Write a function that prints an integer.

     Prototype: def safe_print_integer_err(value):
     value can be any type (integer, string, etc.)
     The integer should be printed followed by a new line
     Returns True if value has been correctly printed (it means the value is an integer)
     Otherwise, returns False and prints in stderr the error precede by Exception:
     You have to use try: / except:
     You have to use "{:d}".format() to print as integer
     You are not allowed to use type()

101. Write a function that executes a function safely.

     Prototype: def safe_function(fct, \*args):
     You can assume fct will be always a pointer to a function
     Returns the result of the function,
     Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
     You have to use try: / except:

102. Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
