lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
list1=[]
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           list1.append(num)
print(list1)
print(list1[-1])
