'''
Exercise 5: Take the following Python code that stores a string:
 str = 'X-DSPAM-Confidence: 0.8475'
 Use find and string slicing to extract the portion of the string after the colon character
and then use the float function to convert the extracted string into a floating point number.
'''
data = 'X-DSPAM-Confidence: 0.8475'
copos = data.find(':')
# print(copos)
piece = str[copos + 1:]
# print(piece)
value = float(piece)    # 虽然piece开头是空格，但是float还是能够成功转换。
print(value)
