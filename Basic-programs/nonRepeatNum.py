from collections import Counter as cs
l=cs([1,2,3,3,4])
z=[k if v==1 else 'a' for k,v in l.items()]
z.remove('a')
print(z)
