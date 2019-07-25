string=input()
liststr=list(string)
print(liststr)
liststr2=[]
list1=[]
for i in string:
        if(i not in  list1):
                val=string.count(i)
                liststr2.append(val)
keys = liststr
values = liststr2
dictionary = dict(zip(keys, values))
k=sorted(dictionary.items(),key=lambda i:i[1],reverse=True)
print(k)
dic=dict(k)
print(dic)
tup=dic.values()
print(tup)
s=set(tup)
print(s)
li=list(s)
li.sort(reverse=True)
print(li)
ans=li[1]
count=0
for key,values in dic.items():
        if(ans==values):
                count+=1
if count==1:
        print('Yes')
elif(count==0):
        print("No")
else:
        print('Invalid')
                
