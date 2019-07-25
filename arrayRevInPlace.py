size=int(input("Enter size"))
list1=[]
for i in range(size):
        num =int(input())
        list1.append(num)
l=len(list1)-1
for i in range(l,-1,-1):
    print(list1[i])
    
