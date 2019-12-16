n=2
m=4
val='cse'
z=len(val)-1
for i in range(n*len(val)-n+1):
    for j in range(m*len(val)-m+1):
        if((i%(len(val)-1)==0)):
            print(val[z],end=' ')
            if(z>=0):
                z-=1
            elif(z<len(val)):
                z+=1
        elif(j%(len(val)-1)==0):
           print(val[1],end=' ')
        else:
           print(end='  ')
    print()

