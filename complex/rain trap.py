
n=[3,2,1,0,3]
n=[3,2,1,0,3,0,3,2,1,2,0,1]
#n=[3,2,1,0,3,2,0,2]
#n=[3,2,1,0,3,2,0,2]
r=0
for i in range(1,len(n)-1):
    a=n[i]
    for j in range(i):
        a=max(a,n[j])
    b=n[i]
    for j in range(i+1,len(n)):
        b=max(b,n[j])
    r=r+(min(a,b)-n[i])
print(r)



	
