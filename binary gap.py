num = int(input("Enter the number:"))
list1=[]
gap=[]
zero=[]
while (1<=num):
    y = num % 2
    x = num//2 
    list1.append(y)
    num = x
print(list1)
value1=int("".join(map(str,list1)))
print(value1)
for i in range (len(list1)):
    if (list1[i]==1):
        gap.append(i)        
print(gap)
for i in range(len(gap)-1):
    x= gap[i+1] - gap[i]-1
    zero.append(x)
print(zero)
if (len(zero)<1):
    print("no binary gap")
else:
    print(max(zero))
    
