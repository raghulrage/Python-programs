exp =  '100 * ( 2 + 12 )'.split()
pre = {'-':0,'+':0,'*':1,'/':1,'^':2}
stack = []
res = []

def highPre(top,data):
    if pre[top]<pre[data]:
        return False
    return True

for i in exp:
    if i.isalnum():
        res.append(i)
    elif i in pre.keys():
        while stack and stack[-1]!='(' and highPre(stack[-1],i) :
            res.append(stack.pop())
        stack.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1]!='(':
            res.append(stack.pop())
        stack.pop()
while stack:
    res.append(stack.pop())
    
print(res)
while len(res) != 1:
    i = 0
    while i<len(res):
        if res[i] in pre.keys():
            s = eval(res[i-2]+res[i]+res[i-1])
            res.pop(i-2)
            res.pop(i-2)
            res.pop(i-2)
            res.insert(i-2,str(s))
            break
        i+=1
print(res)
