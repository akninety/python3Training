def lesser_of_two_evens(a,b):
    return min(a,b)

print(lesser_of_two_evens(100,10))


def animal_crackers(text):
    ac_list = text.split(" ")
    print(ac_list[0][0])
    print(ac_list[1][0])

    if ac_list[0][0] == ac_list[1][0]:
        return True
    else:
        return False

print(animal_crackers("Alex Bnimal"))

def makes_twenty(n1,n2):
    if n1 == 20:
        return True
    elif n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    else:
        return False

print(makes_twenty(10,10))

def old_macdonald(name):
    firstletter = name[0:3]
    fourthletter = name[3:len(name)]

    return firstletter.capitalize() + fourthletter.capitalize()

print(old_macdonald("gordiehowe"))

def master_yoda(text):
    yodaspeak = text.split(" ")
    print(yodaspeak)
    yodaspeak2 = yodaspeak[::-1]
    print(yodaspeak2)
    yodaspeak3 = " ".join(yodaspeak2)
    print(yodaspeak3)

master_yoda("I am home")

def almost_there(n):
    if abs(n-100) <= 10:
        return True
    elif abs(n-200) <= 10:
        return True
    else:
        return False

print(almost_there(244))

def has_33(nums):
    for index,item in enumerate(nums[:-1]):
        if item == 3 and 3 == nums[index+1]:
            return True

    return False

print(has_33([1, 1, 1, 3, 3]))

def paper_doll(text):
    placeholder = ""
    for letter in text:
        placeholder += letter*3

    print(placeholder)


paper_doll("alex")

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if a + b + c <= 21:
        return a + b + c
    if a + b + c > 21:
        if a == 11:
            return a + b + c - 10
        elif b == 11:
            return a + b + c - 10
        elif c == 11:
            return a + b + c - 10
        else:
            return "BUST"

print(blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    sum = 0
    cond = True

    for num in arr:
        if(cond == False):
            if(num == 9):
                cond = True
        elif(num == 6):
            cond = False
        else:
            sum += num
    
    return sum

print(summer_69([4, 5, 6, 7, 8, 9]))
    