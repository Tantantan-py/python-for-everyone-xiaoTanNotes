""" Conditional Steps """

x = 5
if x < 10 :           # 'if' is a reserved word.
    print('Smaller') # The front space is indentding. We tend to indent by 4 spaces. Try not to use 'Tab' unless it would be transformed into 4 spaces automatically.
if x > 20 :
    print('Bigger')
print('Finis')

'''
 <        Less than
 <=       Less than or Equal to
 ==       Equal to                  # Double equals is the question mark version of equality.
 >=       Greater than or Equal to
 >        Greater than
 !=       Not Equal
 '''

''' # Nested Decisions '''
x = 42
if x > 1 :
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

''' # Two-way Decsion With else '''
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')

''' Multi-way with elif ''' # elif is 'else if'
# only one condition triggers though there would be a lot elif.
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All done')

# 随便写的
ix = input('x = ?')
x = int(ix)
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else :
    print('large')

''' Multi-way Puzzles
# Example 1
if x < 2 :
    print('Below 2')
elif x >= 2 : # 直接用else就行，第三部分已经超脱逻辑以外了。
    print('Two or more')
else :
    print('Something else') # This condition will never triggers.

# Example 2
if x < 2 :
    print('Below 2')
elif x < 20 :
    print('Below 20')
elif x < 10 :
    print('Below 10') # This condition will never triggers.
else :
    print('Something else')
'''

''' The try / except Structure '''  # It is a way to eliminate or catch a Traceback.
rawstr = input('Enter your number')
try :
    ival = int(rawstr)
except :
    ival = -1
if ival > 0 :
    print('Nice work')
else :
    print('Not a number')


"""
>>> x = 6
>>> y = 0
>>> x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""
# Correct syntax
'''
>>> x = 6
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False'''
