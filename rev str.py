s=input()
l=[]
l2=[]
for i in range(len(s)):
               if(s[i]==' '):
                   l.append(i)
               else:
                   l2.append(s[i])
print(l,l2)
l2=l2[::-1]
k=0
for i in range(len(s)):
    if(i not in l):
        print(l2[k],end='')
        k+=1
    else:
        print(end=' ')
    
