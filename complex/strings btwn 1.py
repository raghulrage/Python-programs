n=int(input())
for i in range(n):
    num=list(input())
    l=[]
    for i in range(len(num)):
        if(num[i]=='1'):
            l.append(i)
    k=0
    if(len(l)<2):
        print('No string exists')
    else:
        for i in range(0,len(l)-1):
            m=0
            for j in range(len(l)-1):
                m+=1
                s1=l[k]
                s2=l[m]
                if(s1<s2):
                    print(''.join(map(str,num[s1:s2+1])))
            k+=1
#solution 2
a='101101'
for i in range(len(a)-1):
    if(a[i]=='1'):
        for j in range(i+1,len(a)):
            if(a[j]=='1'):
                print(a[i:j+1])
