# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Objects and Data Structures Assessment Test
# %% [markdown]
# ## Test your knowledge. 
# 
# ** Answer the following questions **
# %% [markdown]
# Write a brief description of all the following Object Types and Data Structures we've learned about: 

# %%
Numbers: #So far we've learned how to define a number as int or floats.  Additionally, there's various mathematical operations we can use for numbers(add, subtract, multiply, divide, modulus)

Strings: #Strings are alphanumeric values which can be defined in Python. We've learned how to use them in lists, dictionaries, and sets.

Lists: #Lists are mutable objects in Python and we've learned a few functions associated with them such as appending and popping.

Tuples: #Tuples are immutable objects in Python and have fewer functions associated with them than the other element sets.

Dictionaries: #Dictionaries are elements in Python that have key values associated with data elements.  

# %% [markdown]
# ## Numbers
# 
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# 
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# %%
equation = ((100 * 10) / 100)**2 + 1 - .75
print(equation)

# %% [markdown]
# Answer these 3 questions without typing code. Then type code to check your answer.
# 
#     What is the value of the expression 4 * (6 + 5)
#     
#     What is the value of the expression 4 * 6 + 5 
#     
#     What is the value of the expression 4 + 6 * 5 

# %%
#44
#29
#34

# %% [markdown]
# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>
# %% [markdown]
# What would you use to find a number’s square root, as well as its square? 

# %%
# Square root: sqrt()


# %%
# Square: int**2

# %% [markdown]
# ## Strings
# %% [markdown]
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# %%
s = 'hello'
# Print out 'e' using indexing
print(s[1])

# %% [markdown]
# Reverse the string 'hello' using slicing:

# %%
s ='hello'
# Reverse the string using slicing
print(s[::-1])

# %% [markdown]
# Given the string hello, give two methods of producing the letter 'o' using indexing.

# %%
s ='hello'
# Print out the 'o'

# Method 1:
print(s[4])


# %%
# Method 2:
pring(s[-1])

# %% [markdown]
# ## Lists
# %% [markdown]
# Build this list [0,0,0] two separate ways.

# %%
# Method 1:
my_list = [0,0,0]


# %%
# Method 2:
my_list = [0,0]
my_list.append(0)

# %% [markdown]
# Reassign 'hello' in this nested list to say 'goodbye' instead:

# %%
list3 = [1,2,[3,4,'hello']]
list3.pop()
list3.append('goodbye')

# %% [markdown]
# Sort the list below:

# %%
list4 = [5,3,4,6,1]
list4.sort()

# %% [markdown]
# ## Dictionaries
# %% [markdown]
# Using keys and indexing, grab the 'hello' from the following dictionaries:

# %%
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])


# %%
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])


# %%
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
new_dict = d['k1'][0]
print(new_dict)
new_dict2 = new_dict['nest_key'][1]
print(new_dict2)


# %%
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

new_dict = d['k1'][2]
print(new_dict)
new_dict2 = new_dict['k2']
print(new_dict2)
new_dict3 = new_dict2[1]
print(new_dict3)
new_dict4 = new_dict3['tough'][2]
print(new_dict4)

# %% [markdown]
# Can you sort a dictionary? Why or why not?<br><br>

# %%
#You can sort a dictionary with the sorted() function. We haven't learned that yet?


# %%
## Tuples


# %%


# %% [markdown]
# What is the major difference between tuples and lists?<br><br>

# %%
#Tuples are immutable and lists are not.

# %% [markdown]
# How do you create a tuple?<br><br>

# %%
my_tuple = (1,2,3)

# %% [markdown]
# ## Sets 
# %% [markdown]
# What is unique about a set?<br><br>

# %%
#Sets are an unordered collection of unique lements.

# %% [markdown]
# Use a set to find the unique values of the list below:

# %%
list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))


# %%


# %% [markdown]
# ## Booleans
# %% [markdown]
# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
# 
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>
# %% [markdown]
# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# %%
# Answer before running cell
2 > 3
#False


# %%
# Answer before running cell
3 <= 2
#False


# %%
# Answer before running cell
3 == 2.0
#False


# %%
# Answer before running cell
3.0 == 3
#True


# %%
# Answer before running cell
4**0.5 != 2
#True

# %% [markdown]
# Final Question: What is the boolean output of the cell block below?

# %%
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
#False

# %% [markdown]
# ## Great Job on your first assessment! 
