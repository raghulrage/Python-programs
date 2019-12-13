n=int(input())
k=n-1
for i in range(n):
    alpha=65+i
    for j in range(k):
        print(end=' ')
    k-=1
    for l in range(i+1):
        print("*",end='')
    print(end=' ')
    for x in range(i+1):
        print(chr(alpha),end='')
        alpha+=1
    print()
m=0
for i in range(n):
    z=1+i*2
    for k in range(m):
        print(end=' ')
    m+=1
    for j in range(n,i,-1):
        print(j,end='')
    print(end=' ')
    for x in range(n,i,-1):
        print(z,end='')
        z+=2
    print()

#Solution 2
#-------------------------
for i in range(n*2+1):
    l=[]
    z=65+i
    for j in range(n*2+1):
        if j <n-i-1 :
            l.append(' ')
        if j >=n-i and j <=n and i<n:
            l.append('*')
        if j==n+1:
            l.append(' ')
        if j>n and i<n and j<=n+i+1:
            l.append(chr(z))
            z+=1
        if i>=n:
            if j<=i-n-1 and j<n:
                l.append(' ')

            if j<n and j>=i-n:
                l.append(str(n-j))
            if j>n and i>=n and j<n+i+1 and i<n*2 and j<=+n*2-(i-n):
                l.append(str((j-n)*2-1+(i-n)*2))
                

    print("".join(l))
    
"""
    * A
   ** BC
  *** CDE
 **** DEFG
***** EFGHI
54321 13579
 5432 3579
  543 579
   54 79
    5 9
"""
