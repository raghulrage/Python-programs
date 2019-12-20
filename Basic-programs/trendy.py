num=int(input())
temp=num
if(temp//100==0):
    print("Not a 3 digit number")
else:
    div=num//10
    div=div%10
    if div%3==0:
        print("trend")
    else:
        print("Not")   
