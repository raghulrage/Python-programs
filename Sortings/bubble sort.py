lis = [7,3,2,9,4,5]
n = len(lis)
for i in range(n-1):
    for j in range(n-i-1):
        if lis[j]>lis[j+1]:
            lis[j], lis[j+1] = lis[j+1], lis[j]

print(lis)
