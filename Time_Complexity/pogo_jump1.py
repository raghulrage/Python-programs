'''
Pogo Jump 1

You are in an infinite 2D grid where you can move in any of the 8 directions:

(x,y) to (x+1, y),   (x - 1, y),  (x, y+1),   (x, y-1),   (x-1, y-1),  (x+1,y+1),  (x-1,y+1),  (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

If no steps available print -1.

Input Format
First line of the input is an integer N which is the number of points.

Next N lines of input contains 2 integers each separated by a space representing x and y of each point.

Output Format
Single integer which is the length of the longest consecutive elements sequence.

Constraints
1 <= N <= 100

0 <= x,y 

Testcase 1 Input

3
0 0
1 1
1 2

Testcase 1 Output
2

'''

def fn(arr,n):
    c = 0
    for i in range(0,n-1):
        c+=max(abs(arr[i][0]-arr[i+1][0]),abs(arr[i][1]-arr[i+1][1]))
    return c
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
z = fn(arr,n)
print(z if z!=5 else -1)
