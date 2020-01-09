l=['1','0','2','5']
n=int(input())
k=int(input())
c=0
for i in range(10**(n-1),k):
    x=[j for j in str(i)]
    if(set(x).issubset(set(l))):
        c+=1
print(c)
