'''
1. constants -- 常量；

2. reserved words--保留词(False class return and etc);
# Don't name those reserved words as your variable names.

3. variables -- 变量
#Variables names are places where you are asking Python to allocate memory and stick something in it and label it.

Python Variables Name Rules:
1. Must start with a letter or underscore_
2. Must consist of letters, numbers, and underscores
# Good: spam eggs spam23 _speed
# Bad: 23spam #sign var.12
# Different: spam Spam SPAM
'''

'''Python calculate the Expression firstly, once the expression is evaluated, the result is placed in x,
so the "=" doesn't like the equal in math,
it more likes a wall only accepts the expression result and store it in variable again.
'''

# calls pound sign. It is the comment.

x = 2
x = x + 2
print(x)  # 4

# reminder operation -- % 余数运算
a = 23
b = a % 5
print(b)  # >>>3

# power operation -- ** 次方运算
print(4 ** 3)  # 64

"""" Expression -- right-hand side of assignment statements (右边的赋值语句) """

''' Operator Precedence Rules             运算次序规则：
1. Parentheses are always respected       括号永远优先,
2. Expoentiation (Power)                  其次是幂次指数运算,
3. Multipulation, Division, and Remainder 然后乘、除、余数运算相同
4. Addition and Subtraction               加减法最后
5. Left to right                          从左至右运算
'''
x = 1 + 2 ** 3 / 4 * 5
print(x)  # 11

""" Type """

eee = 'hello ' + 'world'  # this is a string 字符串
print(eee)  # hello world
# 如果不在hello后面打空格space， 那么输出结果也不会有空格

'''如果不是同一种type就不能运算, 不能 string + integer
eee= 'hello '+ 'world'
eee=eee+1
然后Python就不能理解，就会报错 Traceback: Can't convert 'int' object to str implicity(不能将整数对象转化成字符串)
Traceback, which means Python has met something it can't understand and it stopped the programming
and Traceback would tell you where made Python quit
'''

# type命令可以得到该变量的类型
type(eee)  # <class'str'>      #字符串

type('hello')  # <class'str'>      #字符串

type(1)  # <class'int'>      #整数

type(1.0)  # <calss'float'>    #浮点数
# 有小数点的变量称为浮点数 floating point numbers have more range and less precision范围更广，精度更低
print(float(99) + 100)  # 199.0         #199.0 ≠ 199, 命令中直接加入float把结果强行转换成浮点数

ddd = '123'
type(ddd)  # <class'str'>
# 可以通过int函数命令将‘123’转换为整数类型，仅限于字符串内容本身就是数字digits
fff = int(ddd)
type(fff)  # <class'int'>
print(fff + 1)  # 24

""" Input """
# Input reads stuff from the user.
# 手动输入变量(输入的永远被视作一个字符串)，Python交互式输出结果

nam = input('Who are you?')
print('Welcome', nam)
'''
Who are you?
Xu
Welcome Xu
'''

""" Input, Processing, Output programming """
# Convert elevator floors.
inp = input('Europe floor?')  # What we enter is a string.
usf = int(inp) + 1
print('US floor', usf)  # This comma makes a space in result, 这个逗号导致输出结果中间会有空格

# 随便写写
t = input('学号后四位')
try:
    tail = str(t)
except:
    print('Please enter fuor numeric numbers')
    quit()
head = '20193020'
ID = head + tail
print('学号:', ID)
