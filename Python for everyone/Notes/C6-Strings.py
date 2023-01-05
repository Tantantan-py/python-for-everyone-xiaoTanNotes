"""
banana
012345
字符串的位置是从0开始计数的
"""

fruit = 'banana'
letter = fruit[1]   # we pronounce [] 'sub'
print(letter)   # a

x = 3
w = fruit[x - 1]    # we pronounce : fruit sub x minus one
print(w)    # n

''' Find out how long a string is : len function.   '''
fruit = 'banana'
print(len(fruit))   # 6

fruit = 'banana'
x = len(fruit)
print(x)    # 6

''' Looping through Strings '''
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
# 0 b
# 1 a
# 2 n
# # #
# 5 a

# We generally prefer a for loop
fruit = 'banana'
for letter in fruit:
    print(letter)
# b
# a
# #
# a

''' Looping and Counting '''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)    # 3

''' Slicing Strings '''

'''
M o n t y _ P y t h o  n
0 1 2 3 4 5 6 7 8 9 10 11
We can look at any continuous section of a string using a colon operator.
The second number is one beyond the end of the slice - "up to but not including"
If the second number is beyond the end of the string, it stops at the end.
'''

s = 'Monty Python'
print(s[0:4])   # Mont

print(s[6:7])   # P

print(s[6:20])  # Python

print(s[:2])    # Mo

print(s[8:])    # thon

print(s[:])     # Monty Python


''' Using in as a logical Operator '''

'''
The in keyword can also be used to check if one string is 'in' another string
The in keyword is a logical expression thaat returns Ture or False and can be used in an if statement
'''
fruit = 'banana'
'n' in fruit    # True
'm' in fruit    # False
'nan' in fruit  # True
if 'a' in fruit:
    print('Found it!')  # Found it!

''' String Comparison '''
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word' + word + ', comes after banana.')
else:
    print ('All right, bananas.')


''' String Library '''

'''
Python has a number of string functions which are in the String Library,
These functions are already bulit into every string - we invoke them by appending the function to the string variable,
These functions do not modify the oringal string, instead they return a new string that has been altered.
'''
greet = 'Hello Bob'
zap = greet.lower() # make a copy of greet but all lowercase and return it to us.
print(zap)  # hello bob
print(greet)    # Hello Bob
print('Hi There'.lower())   # hi there

'''
You could get the document online for all the string methods:
https://docs#J_goodsList > ul > li .python.org/3/library/stdtypes.html#string-methods
str.capitalize()
str.replace()
str.center(width[, fillchar])
str.lower()
str.endswith(suffix[, start[, end]])
str.rstrip([chars])
str.find(sub[, start[, end]])
str.upper()
'''

''' Searching a String '''
fruit = 'banana'
pos = fruit.find('na')  # To find the position of 'na' in the string.
print(pos)  # 2

aa = fruit.find('z')
print(aa)   # -1

''' Making everything UPPER CASE '''
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)  # HELLO BOB
www = greet.lower()
print(www)  # hello bob

''' Search and Replace '''
# It's very useful.
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)     # Hello Jane
nstr = greet.replace('o','X')
print(nstr)     # HellX BXb

''' Strip Whitespace '''
greet = '   Hello Bob   '
greet.lstrip()  # 'Hello Bob   '    #lstrip : strip(throw away) the left spaces.
greet.rstrip()  # '   Hello Bob'
greet.strip()   # 'Hello Bob'


''' Parsing and Extracting '''
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)    # 21
sppos = data.find('',atpos) # To find the first space starting from the atpos(@position)
print(sppos)    # 31
# Now we have two positions of @ and the ending space, so we are going to slicing the data we need.
host = data[stpos + 1 : sppos]
print(host)     # uct.ac.za

# Actually, we could simply use the .split
wds = line.split()
email = wds[1]
pieces = email.split('@')
print(pieces[1])

''' Prefix '''
line = 'Please have a nice day'
line.startwith('Please')    # True
line.startwith('p')         # False
# using with if statement we could find those start with the prefix we are looking for.


""" String Concatenation """

'''
When the + operatr is appied to strings, it means 'concatenation'
'''
a = 'Hello'
b = a + 'There'
print(b)    # HelloThere

c = a + ' ' + 'There'
print(c)    # Hello There
