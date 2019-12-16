n=int(input())
for i in range(n,0,-1):
    z=((i*(i-1))//2)+1
    for j in range(i):
        print(z,end=' ')
        z+=1
    print()
