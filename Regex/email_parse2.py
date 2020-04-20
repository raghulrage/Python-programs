'''
Write a program to extract all mail id’s from the given input string.

User must get dynamic input.If the string does not contain any mail id's then display 'Mail id is not present' .



Note:

email ids can be in any format

Example:

zuck@yahoo.com,zuck@yahoo.co.in
'''

import re 
n = input()
l = []
for i in re.findall('\S+@\S+',n):
    l.append(i)
if l:
    print('\n'.join(l))
else:
    print('Mail id is not present')
