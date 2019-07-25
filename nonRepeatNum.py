size=int(input("Enter size"))
list1=[]
list2=[]
list3=[]
for i in range(size):
        num =int(input())
        list1.append(num)
for i in range(len(list1)):
    if list1[i] not in list1:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
list1.sort()
print(list1[0])
