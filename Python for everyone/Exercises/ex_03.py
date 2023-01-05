# Exercise 1 : Rewrite your pay computer to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
from re import A

hours = input('Enter Hours:')
rate = input('Enter Rate:')
h = int(hours)
if h <= 40:
    pay = float(hours) * float(rate)
    print('Pay:', pay)
else:
    pay = ((float(hours) - 40) * 1.5 + 40) * float(rate)
    print('Pay:', pay)

# Exercise 2 : Rewrite your pay program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program.
hours = input('Enter Hours:')
try:
    h = float(hours)
except:
    print('Error, please enter numeric input')
    quit()  # Stop here otherwise Traceback occurs owing to h or r is not defined.
rate = input('Enter Rate:')
try:
    r = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
if h <= 40:
    pay = float(hours) * float(rate)
    print('Pay:', pay)
else:
    pay = ((float(hours) - 40) * 1.5 + 40) * float(rate)
    print('Pay:', pay)

''' pythonlearn
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:
 Score    Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
<  0.6     F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for input.'''

# Exercise 3:
grade = input('Enter score:')
try:
    grade = int(grade) and grade>0 and grade<1
    if grade >= 0.9:
        print('A')
    elif grade >= 0.8:
        print('B')
    elif grade >= 0.7:
        print('C')
    elif grade >= 0.6:
        print('D')
    else:
        print('F')
except:
    print('Bad score')


grade = input('Enter score:')
try:
    grade = float(grade) and grade in range(0, 1)
except:
    print('Bad score')
levels = ['A', 'B', 'C', 'D']
s = [0.9, 0.8, 0.7, 0.6]
for score in s:
    if grade >= score:
        break
        pos = s.index(score)
        print(levels[pos])
    else:
        print('F')
