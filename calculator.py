"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    user_input = raw_input("input : ")
    tokens = user_input.split(" ")
    
    if len(tokens) == 3:

        if tokens[1].isdigit() and tokens[2].isdigit():
            n1 = int(tokens[1])
            n2 = int(tokens[2])
        
            if tokens[0] == "+":
               print add(n1, n2)

            if tokens[0] == "-":
                print subtract(n1, n2)

            if tokens[0] == "*":
                print mul(n1, n2)

            if tokens[0] == "/":
                print div(n1, n2)

            if tokens[0] == "pow":
                print power(n1, n2)

            if tokens[0] == "mod":
                print mod(n1, n2)

    elif len(tokens) == 2:

        if tokens[1].isdigit():
            n1 = int(tokens[1])

            if tokens[0] == "square":
                print square(n1)

            if tokens[0] == "cube":
                print cube(n1)

    else:
        print "Please enter valid input"
