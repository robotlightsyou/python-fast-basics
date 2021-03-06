#! /usr/bin/env python3

"""
This program is a basic calculator providing the user addition,
subtraction, multiplication, float division, integer division,
and the modulo operation.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def fdiv(a, b):
    return a / b


def idiv(a, b):
    return a // b


def mod(a, b):
    return a % b


print(mod(68, 3))
print(idiv(68, 3))
print(mult(68, 3))

# if __name__ == "__main__":
#     print("oops, I didn't mean to run this")
# print(mod(68, 3))
# print(idiv(68, 3))
# print(mult(68, 3))
