d={'{':'}','(':')','[':']'}
n=list(input())
l=[]
f=[]
for i in n:
    if(i in d.keys()):
        l.append(i)
    else:
        if(l!=[]):
            if d[l[-1]]==i:
                l.pop()
        else:
            f.append(1)

if(f==[] and l==[]):
    print('True')
else:
    print('False')
