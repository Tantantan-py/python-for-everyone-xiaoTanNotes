"Tuples are like an UNMODIFIED Lists"

"But... Tuples are 'immutable'"
# for a lsit: (mutable)
x = [9, 8, 7]
x[2] = 6
print(x)
# [9, 8, 6]

# for a string: (immutable )
y = 'ABC'
y[2] = 'D'
# Traceback

# for a Tuple: (immutable)
z = (5, 4, 3)
z[2] = 0
# Traceback

""" Tuples and Assignment """
(x, y) = (4, 'fred')
print(y)
# fred
(a, b) = (99, 98)
print(a)
# 99
# WE can even omit the parentheses

""" Tuples and Dictionaries """
# The items() method in dictionaries retuens a lists of (key, value) tupples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
# csev 2
# cwen 4
tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 2)])

""" Tuples are Comparable """
# Python 会比较第一个不同的element， 然后给出判断结果。
# 有点像高考分数一样那么录取先看语文，语文一样再看数学。。。直到有一门不一样然后判断优先录取哪一个
(0, 1, 2) < (5, 1, 2)
# True
(0, 1, 20000) < (0, 3, 4)
# True
('Jones', 'Sally') < ('Jones', 'Sam')
# True
('Jones', 'Sally') > ('Adams', 'Sam')  # Because J is greater than A, it never looks at the second whatsoever.
# True

""" Sorting Lists of Tuples """
d = {'a': 10, 'b': 1, 'c': 22}
d.items()
# dict([('a':10), ('c':22)], ('b':1)])
sorted(d.items())
# [('a':10), ('b':1), ('c':22)]]

# Using sorted()
d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
t
# [('a':10), ('b':1), ('c':22)]]
for k, v in sorted(d.items()):
    print(k, v)
# a 10
# b 1
# c 22

""" Sort by Values Instead of Key """
c = {'a': 10, 'b': 1, 'c': 22}
tem = list()
for k, v in c.items():
    tem.append((v, k))  # v要放到前面来，因为Python只会比较最开始不同的那个
print(tem)
# [('a':10), ('c':22)], ('b':1)]
tem = sorted(tem, reverse=True)  # 从大到小排，一般照最大值或前几大值常用。
print(tem)
# [('c':22)], ('a':10), ('b':1)]

""" The top 10 most common words """
fhand = open(romeo.txt)
counts = dict()
for line in fhand:
    wds = line.split()
    for wd in wds:
        count[wd] = counts.get(wd, 0) + 1
# 以下可以直接缩短成一句。
lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
    print(k, v)

# 但是后半部分可以直接用一行代码完成：
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))
# List comprehension(列表推导) creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
# https://wiki#J_goodsList > ul > li .python.org/moin/HowTo/Sorting
