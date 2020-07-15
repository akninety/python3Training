import math
import string

def vol(rad):
    return 4.0/3.0*math.pi* rad**3

print(vol(2))

def ran_check(num,low,high):
    if num >= low and num <= high:
        print("{} is in the range between {} and {}.".format(num,low,high))
    else:
        print("{} is NOT in the range between {} and {}.".format(num,low,high))

ran_check(5,1,10)

def ran_bool(num,low,high):
    if num >= low and num <= high:
        return True
    else:
        return False

print(ran_bool(50,1,10))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    upper = []
    lower = []
    for characters in s:
        if characters.isupper():
            upper.append(characters)
        elif characters.islower():
            lower.append(characters)
        else:
            pass
    print(upper)
    print(lower)
    print("Original Phrase: {}".format(s))
    print("There are {} upper-case letters.".format(len(upper)))
    print("There are {} lower-case letters.".format(len(lower)))

up_low(s)


def unique_list(lst):
    values = []
    for items in lst:
        if items not in values:
            values.append(items)
    return values

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


def multiply(numbers):
    product = 1
    for nums in numbers:
        product = product * nums
    return product


print(multiply([1,2,3,-4]))

def palindrome(s):
    rev = s[::-1]

    if rev == s:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")


palindrome('hellehs')

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet_set = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return alphabet_set == str1

print(ispangram("The quick brown fox jumps over the lazy dog"))