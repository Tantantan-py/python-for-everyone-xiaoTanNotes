# ex_02_02
"""Write a program that uses input to prompt a user for thier name then welcomes them. """
nam = input('Enter your name:')
print('nam')

# ex_02_03
''' Write a program to prompt the user for hours and rate per hour to compute gross pay. '''
xh = input('Hours:')
xr = input('Rate:')
xp = float(xh) * float(xr)
print('Pay:', xp)

'''
# pythonlearn

2.15 Exercises
Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
Enter your name: Chuck
Hello Chuck

Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
We won’t worry about making sure our pay has exactly two digits after the decimal place for now. If you want,
you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
1. width//2 2. width/2.0 3. height/3 4. 1 + 2 * 5
Use the Python interpreter to check your answers.

Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
and print out the converted temperature.
'''
# 2.15 Exercises2
inp = input('Enter your name:')
print('Hello', inp)

# Exercise 3:
xh = input('Enter Hours:')
xr = input('Enter Rate:')
pay = float(xh) * float(xr)
print('Pay:', pay)

# Exercise 4:
width = 17
height = 12.0
a = width // 2
type(a)
print(a)
b = width / 2.0
type(b)
print(b)
c = height / 3
type(c)
print(c)
d = 1 + 2 * 5
type(d)
print(d)
"""为什么没有class输出结果。"""
# Exercise 5:
Cel = input('Enter the Celsius temperature:\n')
try:
    Fah = float(Cel) * 9 / 5 + 32
    print('Fahrenheit:', Fah)
except:
    print('Please enter a number')
