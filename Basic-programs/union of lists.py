l1=[6,2,4,3]
l2=[6,6,1,4,7,1]
l3=[]
for i in l2:
    if i not in l1:
        l1.extend([i]*l2.count(i))
    else:
        if(l1.count(i)<l2.count(i)):
            l1.extend([i]*(l2.count(i)-l1.count(i)))
print(l1)
        
#solution2
from collections import Counter as cs
l1=[6,6,2,4,3]
l2=[6,1,4,7,1]
n1=cs(l1)
n2=cs(l2)
for i,j in n1.items():
    if( i in n2):
        if n2[i]>j:
            print((str(i)+' ')*n2[i],end='')
        else:
            print((str(i)+' ')*j,end='')
    else:
        print((str(i)+' ')*j,end='')
for i,j in n2.items():
    if(i not in n1):
        print((str(i)+' ')*j,end='')
