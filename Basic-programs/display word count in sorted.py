from collections import Counter as cs
data='Python 3 is better than python 2'.split()
count=cs(data)
for i,j in sorted(count.items()):
    print(' '*(10-len(i)),end='')
    print('{} :   {}'.format(i,j))
        
'''
         2 :   1
         3 :   1
    Python :   1
    better :   1
        is :   1
    python :   1
      than :   1
'''
