d={'{':'}','(':')','[':']'}
n=list(input())
l=[]
f=0
for i in n:
    if(i in d.keys()):
        l.append(i)
    else:
        if(l!=[]):
            if d[l[-1]]==i:
                l.pop()

if(l==[]):
    print('True')
else:
    print('False')
