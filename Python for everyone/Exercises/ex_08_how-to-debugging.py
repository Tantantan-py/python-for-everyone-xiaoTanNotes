""" 看b站 Wored Exercise: Lists， 对与debugging很有启发"""
han = open(mbox-short.txt)

for line in han:
    wds = line.split()
    if wds[0] != 'From':
        continue
    print(wds[2])
# Traceback: if wds[0] != 'From':   IndexError: list index out of range
# 我们发现实际上成功输出了一个结果，找到了一个Sat，我们去看dataset原文件mbox-short.txt发现就是第一行成功输出了
# 问题是我们不知道python爆炸时在做什么
# 在这种情况下，可以先找到traceback那一行代码，确保在它之前有一个print语句

han = open(mbox-short.txt)

for line in han:
    wds = line.split()
    print('Words:', wds)    # 我们在爆炸之前打印出来我们就知道什么时候会爆炸
    if wds[0] != 'From':
        continue
    print(wds[2])
# 所以继续运行一遍，然后发现能找到正确结果，可是还是发现不出来哪里可能有问题
# 这个时候可以在下一行在输入一个print语句

han = open(mbox-short.txt)

for line in han:
    wds = line.split()
    print('Words:', wds)    # 我们在爆炸之前打印出来我们就知道什么时候会爆炸
    if wds[0] != 'From':
        print('Ignore')     # 不符合条件(第一个字符为From:)的， 就会在下一行显示Ignore
        continue
    print(wds[2])
# 这个时候我们就发现在Traceback之前发生了什么了，有一个Words: []出现了，这个就是空字符的一行，但是还是可以检验它是不是空行

han = open(mbox-short.txt)

for line in han:
    print('Line:', line)    # 每一行都在最开始打印一个Line用以辨识
    wds = line.split()
    print('Words:', wds)    # 我们在爆炸之前打印出来我们就知道什么时候会爆炸
    if wds[0] != 'From':
        print('Ignore')     # 不符合条件(第一个字符为From:)的， 就会在下一行显示Ignore
        continue
    print(wds[2])
# 最后就发现并且确定报错来源了
# because it's a blank line, the split returns no words, so wds[0] is not valid, there are no words in the line. so list index out of range.


# Guarian pattern
han = open(mbox-short.txt)

for line in han:
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':    # guardian code
        continue
    print(wds[2])
