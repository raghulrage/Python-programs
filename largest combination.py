num=input("Enter the number:")
y=[]
list1=num.split()
list1.sort(reverse=True)
for i in list1:
    x = list(map(int,str(i)))
    y.append(x)
#y.sort(key = lambda a: a[0],reverse=True)
for i in range(len(y)-1):
    if(y[i][0]==y[i+1][0]):
        a=min(len(y[i]),len(y[i+1]))
        k=0
        while(a>0):
            if(y[i][k]<y[i+1][k]):
                y[i],y[i+1]=y[i+1],y[i]
                break
            k+=1
            a-=1
for i in y:
    for j in i:
        print(j,end='')
