l=["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"] 
num=[2,3]
k=[]
a=0
val=1
for i in num:
    val*=len(l[i])
def fn(num,n):
    fun(num,0,[],n)
    
def fun(num,c,op,n):
    if(c==n):
        global a
        k.append(''.join(op))
        a+=1
        if(val==a):print('['+','.join(k)+']')
        return
    else:
        for i in range(len(l[num[c]])):
            op.append(l[num[c]][i])
            fun(num,c+1,op,n)
            op.pop()
            if(num[c]==0 or num[c]==1):
                return

n=len(num)
fn(num,n)
