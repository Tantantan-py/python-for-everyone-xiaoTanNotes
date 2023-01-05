"""
 Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
 Once "done" is entered, print out the total, count, and average of the numbers.
 If the user enters anything other than a number, detect their mistake using 'try and except'
 and print an error message and skip to the next number.
"""
num = 0
tot = 0.0
while True:
    sval = input('Enter a number ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num +1
    tot = tot + fval
print(tot, num, tot / num)

"""
Exercise 2: Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum numbers instead of the average.
"""
num = 0
tot = 0
smallest = None
largest_so_far = -1
for value in [4, 5, "bad date", 7, "done"]:
    if value == 'done':
        break
    try:
        value = float(value)
    except:
        continue
    if value > largest_so_far:
        largest_so_far = value
for value in [4, 5, "bad date", 7, "done"]:
    if value == 'done':
        break
    try:
        value = float(value)
    except:
        continue
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    num = num + 1
    tot = tot + value
print(tot, num, largest_so_far, smallest)

num = 0
tot = 0
smallest = 100
largest_so_far = -1
for value in [4, 5, "bad date", 7, "done"]:
    if value == 'done':
        break
    try:
        value = float(value)
    except:
        continue
    if value > largest_so_far:
        largest_so_far = value
    if value < smallest:
        smallest = value
    num = num + 1
    tot = tot + value
print(tot, num, largest_so_far, smallest)
