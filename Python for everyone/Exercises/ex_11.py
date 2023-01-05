"""
Exercise 1:
Write a simple program to simulate the operation of the grep command on Unix.
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
"""
import re

inp = input('Enter a regular expression: ')
hand = open('mbox.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(inp, line):
        count = count + 1
print('mbox.txt had', count, 'lines that matched', inp)

'''
Exercise 2:
Write a program to look for lines of the form
`New Revision: 39772`
and extract the number from each of the lines using a regular expression and the findall() method.
Compute the average of the numbers and print out the average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259
'''
import re

inp = input('Enter file:')
hand = open(inp)
lst = []
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9.]+[0-9.])', line)
    if len(x) > 0:
        lst = lst + x
nums = []
for num in lst:
    nums.append(int(num))
print(nums)
average = sum(nums)/len(nums)
print(average)
