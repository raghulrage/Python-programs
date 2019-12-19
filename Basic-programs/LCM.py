def gcd(a,b):
   x=min(a,b)
   for i in range(1,x):
       if(a%i==0 and b%i==0):
           gcd=i
   return gcd
def lcm(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and(greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input())
num2=int(input())
if(num1<1000 and num1>0 and num2<1000 and num2>0):
    print(lcm(num1,num2))
    print(gcd(num1,num2))
else:
    print("Enter number btwn 1 to 1000")
