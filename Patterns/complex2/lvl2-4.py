n=int(input())
k=n-1
for i in range(n):
    alpha=65+i
    for j in range(k):
        print(end=' ')
    k-=1
    for l in range(i+1):
        print("*",end='')
    print(end=' ')
    for x in range(i+1):
        print(chr(alpha),end='')
        alpha+=1
    print()
m=0
for i in range(n):
    z=1+i*2
    for k in range(m):
        print(end=' ')
    m+=1
    for j in range(n,i,-1):
        print(j,end='')
    print(end=' ')
    for x in range(n,i,-1):
        print(z,end='')
        z+=2
    print()
