import math as m
n=input()
n=n.split(',')
n=list(map(int,n))
l=[]
for i in n:
    i=int(i)
    count=0
    sq=m.sqrt(i)
    sq=int(sq)
    if(sq*sq==i):
        count+=5
    if(i%4==0 and i%6==0):
        count+=4
    if(i%2==0):
        count+=3
    l.append(count)
m=zip(l,n)
m=list(m)
m.sort()
for i in range(len(n)):
    print(m[i][1],end=' ')
