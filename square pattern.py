n=4
"""for i in range(2*n):
    for j in range(2*n+1):
        if((i==0 or i==2*n) and j==n):
            print(end='  ')
        else:
            print("*",end='')
    print()
"""
for k in range(1):
    a=0
    b=0
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=' ')
        for l in range(a):
            print(" ",end=' ')
        a+=1
        print(end=' ')
        
        for x in range(b):
            print(" ",end=' ')
        b+=1
        for y in range(i):
            print("*",end=' ')
        print()
a=n-1
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    for k in range(a):
        print(end='  ')
    print(end=' ')
    for x in range(a):
        print(end='  ')
    a-=1
    for y in range(i+1):
        print("*",end=' ')

    print()
        
