n=int(input())
k=n
for i in range(n+1):
    alpha=65
    for j in range(k):
        print(end=' ')
    k-=1
    for l in range(i):
        print(chr(alpha),end=' ')
        alpha+=1
    print()
k=1
for i in range(n,1,-1):
    for j in range(k):
        print(end=' ')
    k+=1
    for l in range(i-1):
        print(chr(alpha),end=' ')
        alpha+=1
    print()
