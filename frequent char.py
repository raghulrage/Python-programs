string=input()
liststr=list(string)
print(liststr)
liststr2=[]
for i in string:
        val=string.count(i)
        liststr2.append(val)
keys = liststr
values = liststr2
dictionary = dict(zip(keys, values))
k=sorted(dictionary.items(),key=lambda i:i[1],reverse=True)
print(k)
for i in k:
    for j in k:
        if(i[1] not in k[1][1])
            
