st = 'Print only the words that start with s in this sentence'
my_st = st.split(" ")
print(my_st)

for words in my_st:
    if words.startswith('s') == True:
        print(words)

print(list(range(0,11,2)))

for num in range(0,50):
    if num % 3 == 0:
        print(num)

st_2 = 'Print every word in this sentence that has an even number of letters'
my_st2 = st_2.split(" ")
print(my_st2)

for words in my_st2:
    if len(words)%2 == 0:
        print(words)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

numrange = list(range(0,100))
print(numrange)

for num in numrange:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)


st_3 = 'Create a list of the first letters of every word in this string'
my_st3 = st_3.split(" ")
print(my_st3)
first_letter_list = []

for words in my_st3:
    first_letter_list.append(words[0])

print(first_letter_list)