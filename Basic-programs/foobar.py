num=int(input())
if(num%3==0 and num%5==0):
    print("FooBar")
elif(num%3==0):
    print("Foo")
elif(num%5==0):
    print("Bar")
else:
    print("None")
