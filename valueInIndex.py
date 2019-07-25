size=int(input("Enter size"))
list1=[]
N=[0,1,2,3,4,5,6,7,8,9]
for i in range(size):
        num =int(input())
        list1.append(num)
list1.sort()
for i in range(len(N)):
    if N[i] in list1:
        print(N[i])
    else:
        print('-1')
