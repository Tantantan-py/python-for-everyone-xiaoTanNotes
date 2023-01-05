''' Repeat Steps '''

"""
 While Statement
 - indefinite loops 不确定循环
 - just runs until some logical condition is false or you hit a break.
"""
n = 5
while n > 0:
    print(n)
    n = n - 1   # Unlike if statement, with the while statement, it goes up again.
print('Blastoff!')
print(n)
# Blastoff!
# 0

''' An Infinite Loop '''
n = 5
while n > 0:    # n is not changing, and so what happens is there's no way for this true to become false. We need to have an iteration that changes.
    print('Lather')
    print('Rinse')
print('Day off')

''' Another Loop '''
# Zero-trip loop 零行程循环, so this basically functions like an if statement.
n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Day off!')

# Breaking Out of a loop
# The break statement ends the current loop and jumps to the statement immediately following the loop.
while True:
    line == input('> ')
    if line == 'done':
        break   # It escapes the loop directly and instantaneously. Get to the next line beyond the end of the loop.
    print(line)
print('Done!')

"""
> hello there
# hello there

> finished
# finished

> done
# Done!
"""

''' Finishing an Iteration with Continue '''
while True:
    line = input('> ')
    if line = input[0] == '#': # line[0]代表第一个字符。所以只要输入的第一个字符是#那就if结果是True。
        continue    # continue basically says quit on the current iteration and like skipping to the top of the loop.
    if line == 'done':
        break
        print(line)
    print('Done!')

"""
> hello there
# hello there

> # don't print this (这个就没有结果输出)

> print this!
# print this!

> done
# Done!
"""


"""
For Statement
- Definite loop are finite. 确定循环是有限的。
"""

''' A Simple Definite Loop '''
for i in [5,4,3,2,1]:   # we see the iteration variable is explicity just part of the syntax. 迭代变量(i)只是语法的一部分。
    print(i)
print('Blastoff!')
# 5
# 4
# 3
# 2
# 1
# Blastoff!

''' A Definite Loop with Strings '''
friends = ['Joseph', 'Glenn', 'Sally']  # It could be a list of numbers or strings.
for friend in friends:  # Python dosen't understand what plurals are.
    print('Happy New Year', friend)
print('Done!')


''' Finding the Largest Value '''
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(the_num, largest_so_far)
print('After', largest_so_far)
# Before -1
# 9 9
# 41 41
# 12 41
# 3 41
# 74 74
# 15 74
# After 74

''' Counting in a Loop '''
# In general, these are called counters. 计数器
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
# Before 0
#
# After 6

''' Summing in a Loop '''
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)
#
# After 154

''' Average in a Loop '''
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)
#
# After 6 154 25

''' Flitering in a Loop '''
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print 'Large number',value
print('After')
# Before
# Large number 41
# Large number 74
# After

''' Search Using a Boolean Variable '''
# Booleans have True or False.
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        # break 那就停在这不会继续运行了。
    print(found, value)
print('After', found)
# Before False
# False 9
# False 41
# False 12
# True 3
# Ture 74
# Ture 15
# After Ture

''' Find the Smallest Value '''
# None is a type as the absence of a value.
Smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if Smallest is None:    # 'is' and 'is not' are like 'less than' or 'less than or euqal to' or 'not equal to'.
        Smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
# Before
# 9 9
# 9 41
# 9 12
# 3 3
# 3 74
# 3 15
# After 3

# None, is, is not are logical operators, which return True or False. 'is' is a really strong equality.
