num=int(input())
temp=num
sum1=0
if(temp//100==0):
    while temp > 0:  
       digit = temp % 10  
       sum1 += digit ** 3  
       temp //= 10
    if num==sum1:
        print("Amstrong")
    else:
        print("Not an amstrong")
else:
    print("Exceeds to 3 digit")
