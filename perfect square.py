num=int(input())
for i in range(2,num):
    if(i*i==num):
        print("Perfectsquare")
        flag=0
        break
    else:
        flag=1
if(flag==1):
    print("not")
        
