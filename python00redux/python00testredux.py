#1 100.25
print((10 ** 2) + (100 * 10) - (1999.5 / 2))

#2
44
29
34

#3
print(type(3 + 1.5 + 4))

#4
print(100 ** 0.5)
print(10 ** 2)

#5
s = 'Hello'
print(s[1])

#6
print(s[::-1])

#7
print(s[-1])
print(s[len(s)-1])

#8
mylist_1 = [0,0,0]
mydict_1 = {'key1':0, 'key2':0, 'key3':0}
print(mylist_1)
print(mydict_1)

#9
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2] = 'goodbye'
print(list3[2][2])

#10
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#11
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d1 = d['k1']
d2 = d1[0]
print(d2['nest_key'][1])

#12
c = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
c1 = c['k1'][-1]
c2 = c1['k2'][-1]
c3 = c2['tough'][-1]
print(c3)

#13
my_set = {1,2,2,33,4,4,11,22,3,3,2}
print(my_set)