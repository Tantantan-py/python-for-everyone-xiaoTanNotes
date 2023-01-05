''' Opening a File '''

'''
 This is done with the open() function
handel = open(filename,mode)    # If we leave mode out, it's going to be read.
like:
fhand = open('mbox.txt','r')    # 'r'-mode is to read.

If you are tring to open a file that doesn't exist, Traceback comes out.
In such a case, use try and except.
'''

''' The newline Character '''
stuff = 'Hello\nWorld'
print(stuff)
# Hello
# World

stuff = 'X\nY'  # \n inside Python is just one single character.
print(stuff)
'''
X
Y
'''
len(stuff)  # 3     # Because \n is one character not two.


''' File Handle as a Sequence '''

'''
A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
We can use the for statement to iterate through a sequence.
Remember - a sequence is an ordered set.
'''
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
# It will take on the successive lines. If this file has 10 lines, this loop is going to run 10 times.


''' Counting Lines in a File '''
fhand = open('mbox.txt')
count = 0
for lines in fhand:
    count = count + 1
print('Line Count:', count)     # Line Count: 132045

''' If you know the file is relatively small compared to the size of your main memory,
you can read the file into one string using the read method on the file handle.'''
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp)) # 94626
print(inp[:20]) # From stephen.marquar

'''Searching through a file'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # 为了消除一行最后面的\n,不然输出的结果之间会间隔空行。
    if line.startswith('From:'):
        print(line)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()    #  Skip 'unintersting lines'
    if not line.startswith('From:'):    continue    # Process our 'interesting lines'
    print(line) # We got the same reslut above.

# 由于find查找另一个字符串中的某一个字符串的出现情况，如果找不到改字符串，则返回该字符串的位置或-1
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)
# 这个时候输出的结果就是输出了所有带@uct.ac.za的行

'''Letting the user choose the file name'''
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)

"""Wrting files"""
fout = open('output.txt', 'w')
print(fout)
# if the file already exists, opening it in write model clears the old data and
# starts fresh, so be careful! If the file doesn't exist, a new one is created.
line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)

fout.close()

"""Debugging"""
s = '1 2\t 3\n 4'
print(s)
# 1 2  3
#  4
# if you want print/type spaces, tab, and newlines, the bulit-in function repr can help.
print(repr(s))
# '1 2\t 3\n 4'
