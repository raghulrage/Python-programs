n=list(input())
val=input()
l=[]
for i in range(len(n)):
    if(n[i]==val):
        l.append(i)
if val not in n :
    l.append (len(n)-1)
print('Character {} occurs at '.format(val),end='')
if(len(l)>0):
    print('{} {}'.format(l[0]+1,l[-1]+1))
else:
    print(l[i]+1,end='')
