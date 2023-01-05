fname = input('Enter File: ' )
if len(fname) < 1:  fname = 'clown.txt' # 偷懒，这样直接按回车就可以读取这个文件
fhand = open(fname)

di = dict()
for line in fhand:
    wds = line.split()
    for w in wds:
        if w in di:
            di[w] = di.get(w, 0) + 1
# print(di)
# {'key': value, 'key2': value2}
# now we want to find the most common word
for k,v in dic.items():
    theword = None
    largest = -1
    if v > largest:
        theword = k
        largest = v
print('Most common word: ', theword,'; Count: ', largest)
