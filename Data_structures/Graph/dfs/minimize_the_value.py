'''
You are given a binary tree rooted at 1. Initially, all the nodes of the tree have some initial values Vi. Wave operation is to be applied on the tree.

After applying the wave operation,
Value of each node in the tree = Sum of all initial values of nodes in its subtree.

You are required to add 1 more node with value X to the tree such that:
1. The tree remains binary after adding the node to the tree.
2. After applying the wave operation to this tree (the tree after adding node with value X), the sum of tree is minimum.

Sum of tree = sum of values of all nodes in the tree.

Print the minimum sum of the tree.

Input :

First line of input contains 2 integers N and X , number of nodes in the tree and value of new node to add respectively.
Second line contains N space separated integers denoting value of each node.
Each of the following N - 1  lines contains 2 integers u and v , representing edge between node u and node v.
Output :

Print the minimum sum possible after adding node with value X and applying wave operation such that tree remains binary tree.
Constraints :

SAMPLE INPUT 
2 1
1 1
1 2
SAMPLE OUTPUT 
5
Explanation
Tree after adding new node (say it 3):



Adding node 3 to root node and applying wave operation,

Value of node 1= 1+1+1= 3 (sum of initial value of nodes 1,2 and 3 as they form the subtree of node 1)
Value of node 2 = 1
Value of node 3 = 1 
Sum of tree = 3+1+1 = 5 which is the minimum possible sum we can get.
'''
import sys
n, x = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
g = [[] for _ in range(n+2)]
for i in range(n-1):
    a, b = map(int,sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
visited  =  [0]*(n+2)
arr.append(x)
g[6].append(n+1)
g[n+1].append(6)
 
def dfs(node,parent):
    if g[node] == []:
        visited[node] = 1
        return arr[node-1]
    if (visited[node] == 0):
        visited[node] = 1
        a = 0
        for child in g[node]:
            if child != parent:
                a += dfs(child,node)
        arr[node-1] += a 
    return arr[node-1] 
    
dfs(1,0)
print(sum(arr))
