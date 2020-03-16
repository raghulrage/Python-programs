storage_details,initial_storage = {},{}
path,litre = [],0

days = int(input())
#initialization of well
for i in range(int(input())):
    n = input().split()
    storage_details[n[0]] = list(map(int,n[1:]))
    initial_storage[n[0]] = 0

#connection
for _ in range(int(input())):
    n = input().split('_')
    if 'F' == n[0]:
        path.append([n[1]])
    else:
        for i in path:
            if n[0] in i:
                i.append(n[1])
#day starting                
for p in path:
    for line in p:
        litre += storage_details[line][1]
        initial_storage[line] += storage_details[line][1]
print(initial_storage)

while True:
    for i in initial_storage.keys():
        initial_storage[i]-=storage_details[i][0]

    days-=1
    if days==0:
        break
    drained = ['' for _ in range(len(path))]
    for i,j in initial_storage.items():
        if j < storage_details[i][0]:
            for temp in path:
               if i in temp:
                   ind = path.index(temp)
                   break
            drained[ind] = i
    print(drained)
    for d in drained:
        for line in path:
            if d and d in line:
                for l in line:
                    if l!=d:
                        initial_storage[l] = storage_details[l][1]
                        litre+=storage_details[l][1]
                    else:
                        initial_storage[l] = storage_details[l][1]
                        litre+=storage_details[l][1]
                        break
print(litre)

'''
Input  
3
4
C1 100 300
C2 100 300
C3 100 200
C4 100 400
4
F_C1
F_C2
C2_C3
C3_C4
Output
1700

2
4
C1 200 400
C2 200 300
C3 100 100
C4 150 300
4
F_C1
F_C3
C1_C2
C3_C4

3
4
C1 200 300
C2 150 300
C3 200 200
C4 100 400
4
F_C1
F_C3
C3_C4
C1_C2

'''
