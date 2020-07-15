"""
def myfunc():
    print("Hello World")

myfunc()

def myfunc2(name):
    print("My name is {}" .format(name))

myfunc2("Alex")

def myfunc3(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

myfunc3(True)

def myfunc4(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

is_even(2)

def is_greater(a,b):
    if a > b:
        return True
    else: 
        return False

def myyfunc(*args):
    return sum(args)

def myyfunc2(*args):
    return [num for num in args if num % 2 == 0]

def myyfunc2b(*args):
    evens = []
    for num in args:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(myyfunc2(1,2,3))
print(myyfunc2b(1,2,3))


def myfunc(string):
    word = []
    for letter in range(0,len(string)):
        if letter % 2 != 0:
            word.append(string[letter].upper())
        else:
            word.append(string[letter].lower())
    return ''.join(word)

print(myfunc("Alex"))
"""

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)
        

print(lesser_of_two_evens(50,500))

def animal_crackers(phrase):
    phraseList = str.split(phrase)
    
    a = phraseList[0]
    b = phraseList[1]

    if a.startswith(b):
        return True
    else:
        return False

print(animal_crackers("alex doggo"))

def makes_twenty(a,b):
    if a == 20:
        return True
    elif b == 20:
        return True
    elif a + b == 20:
        return True
    else:
        return False

print(makes_twenty(1,15))

def old_macdonald(name):
    output = []

    for i,letter in enumerate(name):
        if i == 0:
            output.append(letter.capitalize())
        elif i == 3:
            output.append(letter.capitalize())
        else:
            output.append(letter)

    print(''.join(output))

old_macdonald("alexiscool")

def master_yoda(text):
    words = text.split(' ')
    yoda_speak = ' '.join(reversed(words))
    return print(yoda_speak)
    
master_yoda("Hello there ok cool")

def almost_there(n):
    if abs(n - 100) <= 10:
        return True
    elif abs(n - 200) <= 10:
        return True
    else:
        return False

print(almost_there(210))


def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


print(has_33([1,3,3]))

def paper_doll(phrase):
    text = ''

    for i in phrase:
        text += i * 3
    return text


print(paper_doll("alex"))

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return "BUST"

print(blackjack(10,11,0))

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,3,5,6,7,8,9]))