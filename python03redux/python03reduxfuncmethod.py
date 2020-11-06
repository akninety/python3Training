import math

def vol(rad):
    return float(4.0/3.0 * math.pi * rad**3)

print(vol(2))

def ran_check(num,low,high):
    if num in range(low,high):
        print(f"{num} is in the range of {low} {high}")
    else:
        print(f"{num} is not in the range of {low} {high}")

print(ran_check(1,2,7))

def ran_bool(num,low,high):
    if num in range(low,high):
        return True
    else:
        return False

print(ran_bool(5,2,7))

def up_low(s):
    upper = 0
    lower = 0

    for letters in s:
        if letters.isupper():
            upper += 1
        elif letters.islower():
            lower += 1
        else:
            pass

    print(f"Number of UPPER case characters: {upper}")
    print(f"Number of LOWER case characters: {lower}")

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(lst):
    empty_list = []

    for item in lst:
        if item not in empty_list:
            empty_list.append(item)
    
    print(empty_list)

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

def multiply(numbers):
    product = 1

    for num in numbers:
        product *= num

    print(product)

multiply([1,2,3,-4])

def palindrome(s):
    reverse_string = ''

    for letters in reversed(s):
        reverse_string += letters

    if reverse_string == s:
        return True
    else:
        return False

print(palindrome('hellea'))

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ","")
    alpha_list = []
    str1_list = []

    for letter in alphabet:
        alpha_list.append(letter)

    for letter in str1:
        str1_list.append(letter.lower())

    alpha_list_set = set(alpha_list)
    str1_list_set = set(str1_list)

    if alpha_list_set == str1_list_set:
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))