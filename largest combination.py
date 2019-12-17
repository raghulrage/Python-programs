def permute(seq):

    if len(seq) <= 1:
        perms = [seq]
    else:
        perms = []
        for i in range(len(seq)):
            sub = permute(seq[:i]+seq[i+1:]) 
            for p in sub:    
                perms.append(seq[i:i+1]+p)

    return perms
x=[7,76,10,415]
n=[]
z=permute(x)
for i in z:
    s=''
    for j in i:
        s=s+str(j)
    n.append(int(s))
print(max(n))

#solution
a = input().split()
max_num_in_list = len(max(a))+1
l1 = [(max_num_in_list*i[:max_num_in_list:] , i ) for i in a ]
l1.sort(reverse=True)
for i in range(len(l1)):
    print(l1[i][1],end="")
