n=input()
n=n[1:]
l=[]
for i in range(0,len(n),2):
    l.append(int(str(n[i:i+2]),16))
print(tuple(l))
