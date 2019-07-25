def fact(n):
    if(n<2):
        return n
    else:
        return (fact(n-1)*n)
n=int(input())
num=fact(n)
print(num)
