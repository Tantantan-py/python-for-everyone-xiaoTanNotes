"""A list is a sequence"""
list_nested = ['spam', 2.0, 5, [10,20]] # The length of this list is four.
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []

print(cheeses, numbers, empty)
# ['Cheddar', 'Edam', 'Gouda'] [17, 123] []

"""Lists are mutable"""
print(cheeses[0])
# Cheddar

numbers = [17, 123]
numbers[1] = 5
print(numbers)
# [17, 5]

cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
# True
'Biden' in cheeses
# False

"""Traversing a list"""
# The most common way traverse the elements of a list is with a for loop.
for cheese in cheeses:
    print(cheese)
# if you want to write or update the elements, you need to indices. A common way to do that is to combine the function of range and len;
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

# A for loop over an empty list never excutes the body:
for x in empty:
    print('This never happens.')

"""List operations"""
# the + operator concatenates lists:
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# [1, 2, 3, 4, 5, 6]

# Similarly, the operator repeats a list a giveb number of times:
[0] * 4
# [0, 0, 0, 0]
[1, 2, 3] * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

"""List slices"""
# The slice operator also works on lists:
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
# ['b', 'c']
t[:4]
# ['a', 'b', 'c', 'd']
t[3:]
# ['d', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
# ['a', 'x', 'y', 'd', 'e', 'f']

"""List methods"""
# append adds a new element to the end of a list.
t = ['a', 'b', 'c']
t.append('d')
print(t)
# ['a', 'b', 'c', 'd']

# extend takes a list as an arguement and appends all of the elements:
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
# ['a', 'b', 'c', 'd', 'e']

# sort arranges the elements of the list from low to high:
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
# ['a', 'b', 'c', 'd', 'e']

'''
t.append(x)     # Right
t = t + [x]     # Right

debugging:
t.append([x])       # WRONG!
t = t.append(x)     # WRONG!
t + [x]             # WRONG!
t = t + x           # WRONG!
'''

"""Deleting elements"""
# If you konw the index of the element you want, you can use pop:
t = ['a', 'b', 'c']
x = t#J_goodsList > ul > li .pop(1)
print(t)
# ['a', 'c']
print(x)
# ['b']

# If you don't need the removed value,you can use del operator to delete one or more elements
t = ['a', 'b', 'c']
del t[1]
print(t)
# ['a', 'c']
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
# ['a', 'f']

# If you know the element you want to remove(but not the index), you can use index:
t = ['a', 'b', 'c']
t.remove('b')
print(t)
# ['a', 'c']
# The return value from remove is None.

"""Lists and Functions"""
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
# 6
print(max(nums))
# 74
print(min(nums))
# 3
print(sum(nums))    # the sun() function only works when the list elements are numbers.
# 154
print(sum(nums)/len(nums))
# 25

# First, the program to compute an average without a list:
total = 0
count = 0
while True:
    inp = input('Enter a number')
    if inp == 'done':   break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average', average)

# Also, we could simply remember each number without set total and count.
numlist = list()
while True:
    inp = input('Enter a number')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average', average)

"""List and strings"""
s = 'spam'
t = list(s)
print(t)
# ['s', 'p', 'a', 'm']

s = 'Donot say the wjord'
t = list.split(s)
print(t)
# ['Donot', 'say', 'the', 'fjord']
print(t[2])
# the

line = 'first;second;third'
thing = line.split(';')
print(thing)


# You can also call split with an optional arguement called a delimiter, e.g. using a hyohen as a delimiter:
s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
['spam', 'spam', 'spam']

# join is the inverse of split.
s = ['Donot', 'say', 'the', 'fjord']
delimiter = ' '
s.join(delimiter)
# 'Donot say the wjord'

"""Parsing lines"""
# What if we wanted to print out the day of the week from those lines that start with “From”?
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# The split method is very effective when faced with this kind of problem.
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):  continue
    wds = line.split()
    print(wds[2])
# Sat
# Fri
# Fri

# 如果只用.split的话，那么就无法处理空行，所以在写代码的时候要记得加上guardian code。
# 如 Exercise 2&3
fhand = open('mbox-short.txt')
try:
    for line in fhand:
        wds = line.split()
        if len(wds) < 3 or wds[0] != 'From': continue    # guardian code
        print(wds[2])
except:
    print('There is no lines that starts with "From" in the file: mbox-short.txt')

"""Objects and values"""
a = 'banana'
b = 'banana'
a is b
# True
# In this example, Python only created one string object, and both a and b refer to it.

a = [1, 2, 3]
b = [1, 2, 3]
a is b
# False
'''
In this case we would say that the two lists are equivalent, because they have the same ele- ments, but not identical,
because they are not the same object. If two objects are identical, they are also equivalent,
but if they are equivalent, they are not necessarily identical.

Until now, we have been using “object” and “value” interchangeably,
but it is more precise to say that an object has a value. If you execute a = [1,2,3],
a refers to a list object whose value is a particular sequence of elements.
If another list has the same elements, we would say it has the same value.
'''

"""Aliasing"""
a = [1, 2, 3]
b = a
a is b
# True
# An object with more than one references has more than one name, so we say that the object is alised.
# If the alised object is mutable, changes made with one alias affect the other.
b[0] = 17
print(a)
# [17, 2, 3]

"""List arguemnts"""
def delete_head(t):
    del t[0]
letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)
# ['b', 'c']
'''
It is important to distinguish between operations that modefies lists and
operations that creats new lists.
For example, the append method modfies a list, but the + operator create a new lists
'''
t1 = [1, 2]
t2 = t1.append(3)
print(t1)
# [1, 2, 3]
print(t2)
# None

t3 = t1 + [3]
print(t3)
# [1, 2, 3]
t2 is t3
# False

'''
This difference is important when you write functions that are supposed to modify lists.
For example, this function does not delete the head of a list:
'''
def bad_delete_head(t):
    t = t[1:]   # WRONG!!!!!
# 这个只是取t里面的从1到最后一个元素到位置，并没有删除第一个元素。

'''
An alternative is to write a function that creates and returns a new list.
For example, tail returns all but the first element of a list:
'''
def tail(t):
    return t[1:]
# This function leaves the orignal list unmodified. Here's how it used:
letters = ['a', 'b', 'c']
tail(letters)
print(letters)
# ['b', 'c']

"""Debugging"""
'''             !! !!
Careless use of lists (and other mutable objects) can lead to long hours of debugging.
'''
