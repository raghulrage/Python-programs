from math import sqrt as q
x=int(input())
print(('yes' if (float(5*x**2-4)==(int(q(5*x**2-4)))*int(q(5*x**2-4)) or float(5*x**2+4)==int(q(5*x**2+4))*int(q (5*x**2+4)))  else 'No'))

'''
if
5(x**2)-4
or
5(x**2)+4
returns a
prfect square
thn x is a part of fibonacci
'''
