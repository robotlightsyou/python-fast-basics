#! /usr/bin/env python3
'''
# start with getting a string from the user
start = input("Please enter the text you want altered: ")

# you have to declare your variable before you can add to it in the loop
output = ""

for letter in start:
    # check the case of the character and return opposite if alphabetical
    # isupper/islower are implicit isalpha checks as not letters aren't cased.
    if letter.isupper():
        output += letter.lower()
    elif letter.islower():
        output += letter.upper()
    else:
        output += letter

print(output)
'''
''' Now lets try putting that into a function so you can call it multiple times'''

def swap_case(string):

    output = ""
    for letter in string:
        if letter.isupper():
            output += letter.lower()
        elif letter.islower():
            output += letter.upper()
        else:
            output += letter
    return output

print(swap_case(input("Please enter the text you want altered: ")))