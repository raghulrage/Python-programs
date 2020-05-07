from collections import defaultdict
def dfs(x):
    v[x]=d[x]
    for i in d1[x]:
        if v[i]==-1:
            dfs(i)
            v[x]+=v[i]
n,q=map(int,input().split())
l=list(map(str,input().split()))
d={}
for i in range(1,n+1):
    d[i]=l[i-1]
'''
You are given a rooted tree with N nodes. Each node contains a lowercase English letter. Node with label 1 is the root.There are Q questions of the form

X S: Here X is the root of subtree and S is a string.

For each question, let T be the string built using all the characters in the nodes of subtree with root X (each subtree node character comes exactly once) .
For each question, print minimum number of characters to be added to T , so that the we can build S using some characters of string T (each character of string T can be used at most once).


Hint: Find all the characters coming in each subtree and use it to get the answer to each question.

Input Format

The first line of input consists of two space separated integers N and Q that are number of nodes in the tree and number of questions respectively.
Next line will contain N space separated lowercase English letters, where  letter will be the letter stored in node with label i .
Each of the next  lines contains two space separated integers u and v that denote there is an edge between nodes with labels u and v .
Next Q lines follow. Each line will contain an integer X that denotes the node label and a string S separated by a single space.

Output Format

For each query, print the required answer in a new line.

Input Constraints





All characters in nodes and string are lowercase English letters.

Sum of lengths of strings in all the questions is at most 

SAMPLE INPUT 
8 3
o v s l v p d i
1 3
8 3
4 8
6 1
5 3
7 6
2 3
7 ifwrxl
4 eyljywnm
3 llvse
SAMPLE OUTPUT 
6
7
2
Explanation
Query 1- Character in the subtree with root 7 is d, we need 6 characters(i,f,w,r,x,l) to make S=(ifwrxl).

Query 2- Character in the subtree with root 4 is l, we need 7 characters(e,y,j,y,w,n,m) to make S=(eyljywnm).

Query 3- Characters in the subtree with root 3 are (v,s,i,l), we need 2 characters(l,e) to make S=(llvse).

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Marks are awarded when all the testcases pass.
'''
d1=defaultdict(list)
for i in range(n-1):
    a,b=map(int,input().split())
    d1[a].append(b)
    d1[b].append(a)
v={}
for i in range(1,n+1):
    v[i]=-1
dfs(1)
for i in range(q):
    x,y=input().split()
    x=int(x)
    d2={}
    for i in v[x]:
        if i not in d2.keys():
            d2[i]=1
        else:
            d2[i]+=1
    cnt=0
    for j in y:
        if j not in d2.keys():
            cnt+=1
        else:
            if d2[j]>0:
                d2[j]-=1
            else:
                cnt+=1
    print(cnt)
 
