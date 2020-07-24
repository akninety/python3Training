def display_list(mylist):
    print(mylist)

mylist = [0,1,2,3,4,5,6,7,8,9,10]
display_list(mylist)

result = input("Please enter a value: ")
print(type(result))

resultNum = int(input("Please enter a number: "))
print(type(resultNum))

def user_choice():
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    choice = input("Please input a number (0-10)")
    
    return int(choice)

user_choice()