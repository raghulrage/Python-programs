'''
Avengers after getting defeated from Thanos called zeta for help.

zeta and Thanos are having a one on one battle in Wakanda. The land of Wakanda consists of a N x M grid.

Every block of the grid can contain elements only from the following set: {0,1,2,3,4,5,6,7,8,9,*}

From a block zeta can move UP, DOWN, LEFT or RIGHT but he cannot go to the block containing * because that block is a warmhole to another dimesion where "Children of Thanos" will kill zeta.

To know his fate before hand, Thanos is using the "Time Stone" to see Q different possibilities.

In each of the Q possibility the position of zeta is (x,y) but that of Thanos changes.

For the ith possibility the position of Thanos is ().

Every time, zeta starts moving towards Thanos and takes the path having shortest distance so that he can reach to Thanos before he snaps his fingers again. :( (RIP Spidey!!)

Distance of the following blocks from (i,j) is 1:

(i+1,j)  (i-1,j)  (i,j+1)  (i,j-1)

If more than one paths are possible with the same shortest distance, zeta takes the path resulting in largest sum of block elements. (If zeta travels from (1,1) -> (1,2) -> (2,2) the sum of block elements will be 5.)


Since Thanos is not an easy villian you need to help zeta in finding the shortest distance and its corresponding sum of block elements.

 

 

Input Format:

First line contains two space seperated integer N and M.

Next N lines contain M space seperated charcters from the following set: {0,1,2,3,4,5,6,7,8,9,*}

Next line contains to space seperated integers X and Y denoting the positiob of zeta.

Next line contains an integer Q denoting the number of possibilities Thanos sees using the "Time Stone".

Next Q lines contain two space seperated integers () denoting Thanos's position in each posibility.

It is guaranteed that initial position of zeta WILL NOT be a '*'. It will always be a block having a number from [0 9].

 

Output Format:

Print two space seperated integer "Shortest distance to reach thanos" and "corresponding sum of block elements"(Remember that if more than one path with the same shortest distance are possible you need to consider the one with the largest sum of block elements) .

If Thanos is himself standing on * block in any of the posibility, print "-1 -1" (without qoutes).

If zeta is not able to reach Thanos, print "-1 -1" (without qoutes).

 

 

INPUT CONSTRAINTS

SAMPLE INPUT 
2 2
7 *
2 5
1 1
2
2 2
2 1
SAMPLE OUTPUT 
2 14
1 9
'''
import queue
 
def bfs(arr, m, n, r0, c0, a, b):
    dr = [-1, 0, 1,  0]
    cr = [ 0, 1, 0, -1]
    a[r0][c0] = 0
    b[r0][c0] = int(arr[r0][c0])
    Q = queue.Queue(0)
    Q.put([r0, c0, 0])
    while not Q.empty():
        r, c, d = map(int, Q.get())
        for i in range(4):
            rr = r + dr[i]
            cc = c + cr[i]
            if rr >= m or rr < 0:
                continue
            if cc >= n or cc < 0:
                continue
            if (arr[rr][cc] =="*"):
                continue
            if (a[rr][cc] > d + 1):
                a[rr][cc] = d + 1
                b[rr][cc] = b[r][c] + int(arr[rr][cc])
                Q.put([rr, cc, d + 1])
            elif (a[rr][cc] == d + 1) and (b[rr][cc] < int(arr[rr][cc]) + b[r][c]):
                a[rr][cc] = d + 1
                b[rr][cc] = int(arr[rr][cc]) + b[r][c]
                Q.put([rr, cc, d + 1])
 
def solve():
    m, n = map(int,input().split())
    a = [[] for i in range(m)]
    for i in range(m):
        a[i] = list(input().split())
 
    x0, y0 = map(int, input().split())
    x0 -= 1
    y0 -= 1
    path = [[10000000 for j in range(n)] for i in range(m)]
    val = [[0 for j in range(n)] for i in range(m)]
    bfs(a, m, n, x0, y0, path, val)
    Q = int(input())
    for i in range(Q):
        x1, y1 = map(int,input().split())
        x1 -= 1
        y1 -= 1
        r1 = path[x1][y1]
        r2 = val[x1][y1]
        if r1 == 10000000:
            r1 = r2 = -1
        print(r1,r2)
 
solve()
