""" Summary """
'''
^ Matches the beginning of the line
$ Matches the end of the line
. Matches any character(a wildcard)
\s Matches a whitespace character
\S Matches a non-whitespace character(opposite of \s)

[aeiou] Matches a single character as long as that character is in the specified set. Inside[] could be any words you want.
[a-zA-Z0-9] You can specify ranges of characters using the minus sign.
[^A-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single characters
          that is anything other than an uppercase or lowercase letter.
() When parentheses are added to a regular expression, they are ignored for the purpose of matching,
    but allow you to extract a particular subset of the matched string rather than the whole string when using findall().

\b Matches the empty string, but only at the start or end of a word.
\B Matches the empty string, but not at the start or end of a word.
\d Matches any decimal digit; equivalent to the set[0-9].
\D Matches any non-digit character; equivalent to the set[^0-9]
'''

# Search for lines that contain 'From'
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Search for lines that start with 'From'
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

""" Character matching in regular expression """
# Search for lines that start with 'F', followed by 2 character, followed by 'm:'
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# Search for lines that start with From and have an @ sign
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):  # ".+" means followed by one or more character.
        print(line)
# .* match zero-or-more characters

""" Extracting data using regular expression """
# We use findall() method to extract all the substrings which match a regular expression.
# findall() returns a list
import re

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)  # The \S+ matches as many non-whitespace characters as possible.
print(lst)
# ['csev@umich.edu', 'cwen@iupui.edu']
# It would not match the @2PM because there are no non-blank characters before the at-sign.

# Search for lines that have an at-sign between characters
import re

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
# But some email address have incorrect characters like "<" or ";" at the beginning or end.
# We use Square brackets to indicate a set of multiple acceptable characters we want to consider matching.
# [a-zA-Z0-9]
# Translation: We are looking for a substrings that start with a single lowercase/uppercase letter, or numbers.
import re

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', line)
    if len(x) > 0:
        print(x)

""" Combining searching and extracting """
'''
If we want to find numbers on lines that start with the string "X-" such as:
X-DSPAM-Confidence: 0.0845
X-DSPAM-Probability: 0.0000
'''
# Firstly we could figure it out how to select lines: ^X-.*: [0-9.]
# Note that inside the square brackets, the period matches actually a period.(句号)
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('X-.*: [0-9.]+', line):
        print(line)
# But now we have to solve the problem of extracting the numbers Only.

# ! When you are using findall(), parentheses indicate that while you want the whole expression to match,
# you only are interested in extracting a portion of the substring that matches the regular expression.
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('X-.*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

'''
As another example of this technique, if you look at the file there are a number of lines of the form:
Details: https://source.sakaiprojet.org/viewsvn/?view=rev&rev=39772
If we want to extract all of the version numbers?
'''
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

'''
We looked for lines of the form:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
and want to extract the hour of the day for each line.

Previously we did this with two calls to split. Fist the line was split into word
and then we pulled out the fifth word and split it again on the colon character to pull out the two characters we are interested in.

NOW! We could using findall():
'''
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('From.*([0-9][0-9])', line)
    if len(x) > 0:
        print(x)
# ['09']

""" Escape character """
'''
We can indicate that we can find money amounts with the following regular expression
'''
import re

x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
# Since we prefix the dollar sign with a backslash, it actually matches the dollar sign in the input string
# instead of matching the "end of line".

""" Debugging """
import re

dir(re)
# You can use the dir() to find the methods in the module.
