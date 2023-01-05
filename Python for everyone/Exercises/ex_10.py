""" Tuples and Sorting """
fname = input('Enter File: ' )
if len(fname) < 1:  fname = 'clown.txt'
fhand = open(fname)

di = dict()
for line in fhand:
    wds = line.split()
    for w in wds:
        if w in di:
            di[w] = di.get(w, 0) + 1
tem = list()
for k,v in di.items():
    newt = (v,k)
    tem.append(newt)
tem = sorted(tem, reverse = True)
for v,k in tem[:5]:
    print(k,v)

"""
Exercise 1:
 Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
 Count the number of messages from each person using a dictionary.

 After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
 Then sort the list in reverse order and print out the person who has the most commits.

 Sample Line:
 From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

 Enter a file name: mbox-short.txtcwen@iupui.edu 5

 Enter a file name: mbox.txtzqian@umich.edu 195
 """
inp = ('Enter a file name: ')
hand = open(inp)
counts = dict()
for line in hand:
    line = line.rstrip()
    if not line.startswith('From'): continue

    wds = line.split()
    for wd in wds:
        count[wd] = counts.get(wd,0) + 1
