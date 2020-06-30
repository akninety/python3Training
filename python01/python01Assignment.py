st = 'Print only the words that start with s in this sentence'
new_st = st.split(" ")
print(new_st)

for words in new_st:
    if words.startswith('s'):
        print(words)

print(list(range(0,11,2)))

numberSet = list(range(1,50))
print(numberSet)

for byThree in numberSet:
    if byThree % 3 == 0:
        print(byThree)

st2 = 'Print every word in this sentence that has an even number of letters'
st2_split = st2.split(" ")
print(st2_split)

for evenWords in st2_split:
    if len(evenWords) % 2 == 0:
        print(evenWords)

newRange = list(range(0,100))
print(newRange)

for numbs in newRange:
    if numbs % 3 == 0 and numbs % 5 == 0:
        print("FizzBuzz")
    elif numbs % 5 == 0:
        print("Buzz")
    elif numbs % 3 == 0:
        print("Fizz")
    else:
        print(numbs)

st3 = 'Create a list of the first letters of every word in this string'
st3_split = st3.split(" ")
print(st3_split)

for firstLetters in st3_split:
    print(firstLetters[0])