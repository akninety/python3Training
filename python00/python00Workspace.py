equation = ((100 * 10) / 100)**2 + 1 - .75
print(equation)

s = 'Hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])

my_list = [0,0]
my_list.append(0)
print(my_list)

list3 = [1,2,[3,4,'hello']]
list3.pop()
list3.append('goodbye')
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
new_dict = d['k1'][0]
print(new_dict)
new_dict2 = new_dict['nest_key'][1]
print(new_dict2)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
new_dict = d['k1'][2]
print(new_dict)
new_dict2 = new_dict['k2']
print(new_dict2)
new_dict3 = new_dict2[1]
print(new_dict3)
new_dict4 = new_dict3['tough'][2]
print(new_dict4)

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])