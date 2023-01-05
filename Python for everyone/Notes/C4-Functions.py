''' Functions '''
# D-R-Y: Don't Repeat Yourself.

''' Stored (and reused) Steps '''
def thing():    # def: define a function
    print('Hello')
    print('Fun')
thing()
print('Zip')
thing()


''' Max function '''

big = max('Hello world')
print(big) # w
# 字母排序里面。小写比大写要大。
tiny = min('Hello wrold')
print(tiny) # the answer is a space

''' Building Function '''

x = 5
print('Hellp wrold')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyrics() # def doesm't run itself automatically, you must invoke.
x = x + 2
print(x)

''' Parameters - 参数 '''
def greet(lang):    # lang is a Parameter.(alias)
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en') # Hello
greet('es') # Hola
greet('fr') # Bonjour

''' Return Values '''
# return命令做了两件事： One, it stops function, and it jumps to next line; Two, it also determines the residual values(返回值)
def greet():
    return 'Hello'
print(greet(), 'Gleen') # Hello Gleen
print(greet(), 'Sally') # Hello Sally

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'Gleen') # Hello Gleen
print(greet('es'), 'Sally') # Hola Sally
print(greet('fr'), 'Michael')   # Bonjour Michael

# Multiple Parameters
def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)    # 8
