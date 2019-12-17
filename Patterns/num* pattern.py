n = 5
c =1
for i in range(n):
    for j in range(i+1):
        print(c,end="")
        c+=1
        if j != i :
            print('*',end="")
    print()
c-=1
a=1
z=0
for i in range(n-1,-1,-1):
    b=c
    b=b-n+a+z
    for j in range(i+1):
        print(b,end="")
        b+=1
        if j != i :
            print('*',end="")
        a-=1
    z+=1
    print()
'''
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
'''
