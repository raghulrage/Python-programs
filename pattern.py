num=int(input())
k=1
for i in range(num):
    for j in range(0,i+1):
        print(k,end=' ')
        k+=1
    print()
