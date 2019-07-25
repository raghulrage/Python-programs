amount=int(input())
list1=[500,100,50,20,10,5,2,1]
list2=[]
temp=amount
for i in list1:
    if(temp//i>0):
        var1=temp//i
        list2.append(var1)
        temp=temp%i
    else:
        list2.append(0)
for i in range(len(list1)):
    print(list1[i],':',list2[i])
