"""pythonlearn"""
'''
Exercise 1:
Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.'''

babibobo = ['1', '2', '3', '4', '5']


def chop(t):
    del t[0]
    del t[-1]
    return None


chop(babibobo)
print(babibobo)


def middle(t):
    return t[1:-1]


middle(babibobo)
print(babibobo)

"""Exercise 2:"""
fhand = open('mbox-short.txt')
for line in fhand:
    wds = line.split()
    if len(wds) == 0:   continue
    if wds[0] != 'From':  continue
    print(wds[2])

"""Exercise 3:"""
fhand = open('mbox-short.txt')
try:
    for line in fhand:
        wds = line.split()
        if len(wds) < 3 or wds[0] != 'From': continue  # 第一层guardian code消灭了空行的影响。
        print(wds[2])
except:
    print('There is no lines that starts with "From" in the file: mbox-short.txt')

"""Exercise 4:"""

fname = input('Enter file')   # romeo.txt
fhand = open(fname)
t = []
for line in fhand:
    wds = line.split()
    for word in wds:
        if not word in t:
            t.append(word)
print(t.sort())


"Exercise 5: Minimalist Email Client."
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    wds = line.split()
    if len(wds) == 0 or wds[0] != 'From' or wds.startswith('From:'):
        continue
    count = count + 1
    print(wds[2])
print('There were', count, 'lines in the file with From as the first word')

"""Exercise 5:"""
while True:
    inp = input('Enter a number: ')
    if inp == 'done':   break
    value = int(inp)
    print(value)
    t = []
    t = t.append(value)
t_s = t.sort()
print('Maximun:', float(t_s[-1]))
print('Minimun:', float(t_s[0]))

import os
print(os.getcwd())
