'''
List is a linear collection of values that stay in order

Dictionary is a "bag" of values, each with its own label
'''

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
# {'money': 12, 'tissues': 75, 'candy': 3}
print(purse['candy'])
# 3
print('candy') = purse['candy'] + 2
print(purse['candy'])
# 5

"""Comparing Lists and Dictionaries"""
lst = list()
lst.append(21)
lst.append(183)
print(lst)
# [21, 183]
lst[0] = 23
print(lst)
# [23, 183]

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# {'course': 182, 'age': 21}    dict usually messes order.
ddd['age'] = 23
print(ddd)
# {'course': 182, 'age': 23}

""" Dictionary Literals(Constants) """
# Pairs of " key : value"
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
# {'fred': 42, 'chuck': 1, 'jan': 100}
ooo = {}
print(ooo)
# {}

""" Counting with Dictionary """
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# the get Method for Dictionary
'''The pattern of checking to see if a key is already in a dictionary and assuming a default value
if the key is not there is so common that there is a method called get() that does this for us.'''
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0) # What counts.get is, it says go look up in counts, use 'name' as the key,
                        # and '0 ' as the default, Meaning this is the value i get back if the key doesn't exist.

# 上面是原理，下面是coding

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1  # get the current count of the name Or 0 and then add 1 to it.
print(counts)

"""Dictionaries and files"""

# Counting Pattern
counts = dict()
print('Enter a line of text: ')
line = inp('')
words = line.split()
print('Words: ', words)
print('Counting')
for word in words:
    counts[word] = countss.get(word, 0) + 1
print('Counts', counts)

# Definite Loops and Dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
# jan 100
# chuck 1
# fred 42

# Retrieving lists of Keys and values
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))    # We are telling Python to convert this dic variable to a list.
# ['jan', 'chuck', 'fred']
print(jjj.keys())
# ['jan', 'chuck', 'fred']
print(jjj.values())
# 100, 1, 42
print(jjj,items())
# [('jan', 100), ('chuck', 1), ('fred', 42)]
# These out of things are three tuples.

# Bonus: Two Iteration variables!!
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for k,v in jjj.intems():    # It gives back keys and values.
    print(k,v)

""""Find the most frequent used word and count it""""
name = input('Enter a name')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        count[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for k,v in counts.items():
    if bigword = None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)
