#! /usr/bin/env python3
'''
Ask the user for input, modify the return
'''
def main():
    print(swap_case())

def swap_case():

    print("Please enter a string to alter. ")
    start = input(">")
    end = ""

    for letter in start:
        if letter.isupper():
            end += letter.lower()
        elif letter.islower():
            end += letter.upper()
        else:
            end += letter

    return end

if __name__ == "__main__":
    main()