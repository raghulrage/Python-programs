l1,l2=[],[]
n=int(input())
for i in range(n):
    l1.append(int(input()))
for j in range(n):
    l2.append(int(input()))
for i,j in zip(l1,l2):
    s=[]
    m=0
    for x in range(2,j//2+1):
        for c in range(2,x+1):
            if(x not in s):
                if(x%c==0 and x!=c):
                    break
        else:
            s.append(x)
    for k in range(i,j+1):
        for l in s:
            if(k/l in s):
                m+=1
                break
print(m)

'''
find semi prime number between the range
4 #no of input
1
2
3
4
--------------------1st list
12
23
24
25
------------------2nd list
find semi prime btwn 1st list and 2nd list (1,12)(2,23).....
'''
