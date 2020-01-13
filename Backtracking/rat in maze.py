#LEVEL-1:
maze = [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [1,0,1,0,0],
    [0,0,0,0,0],
    [1,1,1,0,0]
]
SIZE= len(maze)

solution = [[0]*SIZE for _ in range(SIZE)]

def solvemaze(l,r):
    if l==SIZE-1 and r==SIZE-1:
        solution[l][r]=1
        return True
    if l<SIZE and r<SIZE and l>=0 and r>=0 and solution[l][r]==0 and maze[l][r]==0:
        solution[l][r]=1
        if solvemaze(l+1,r):
            return True
        if solvemaze(l-1,r):
            return True
        if solvemaze(l,r+1):
            return True
        if solvemaze(l,r-1):
            return True
        solution[l][r]=0
        return False
    return 0

if solvemaze(0,0)==True:
    for i in maze:
        print(i)
    print()
    for i in solution:
        print(i)
else:
    print("no solution")  

#LEVEL-3
maze = [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,0,0,1],
    [1,1,1,0,0]
]
SIZE= len(maze)
d=0
ans=[]
mindis=[]
solution = [[0]*SIZE for _ in range(SIZE)]

def solvemaze(l,r):
    global d
    if l==SIZE-1 and r==SIZE-1:
        d+=1
        solution[l][r]=1
        mindis.append(d)
        dis=0
        ans.append(copy.deepcopy(solution))
        if(d not in mindis):
            return True
        d-=1
        return False

    if l<SIZE and r<SIZE and l>=0 and r>=0 and solution[l][r]==0 and maze[l][r]==0:
        solution[l][r]=1
        d+=1
        if solvemaze(l+1,r):
            return True
        if solvemaze(l-1,r):
            return True
        if solvemaze(l,r+1):
            return True
        if solvemaze(l,r-1):
            return True
        solution[l][r]=0
        d-=1
        return False
    return 0

if solvemaze(0,0)==True:
    pass
else:
    if(mindis==[]):
        print("no solution")
    else:
        print(min(mindis))
        for i in ans[mindis.index(min(mindis))]:
            print(i)
        
#LEVEL-4
maze = [
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
]
N= len(maze)
dist=[0]
solution = [[0]*N for _ in range(N)]

def solvemaze(l,r,dist):
    if maze[0][0]==1 and maze[N-1][N-1]==1 and maze[0][N-1]==1 and maze[N-1][0]==1:
        return False
    if ((l==N-1 and r==N-1) or (l==0 and r==N-1) or(l==0 and r==0) or (l==N-1 and r==0)) and maze[l][r]!=1:
        solution[l][r]=1
        dist[0]+=1
        return True
    if l<N-1 and r<N-1 and l>=0 and r>=0 and solution[l][r]==0 and maze[l][r]==0:
        solution[l][r]=1
        dist[0]+=1
        if solvemaze(l-1,r,dist):
            return True
        if solvemaze(l,r-1,dist):
            return True
        if solvemaze(l+1,r,dist):
            return True
        if solvemaze(l,r+1,dist):
            return True
        
        solution[l][r]=0
        dist[0]-=1
        return False
    return 0


if solvemaze(2,3,dist):
    for i in maze:
        print(i)
    print()
    for i in solution:
        print(i)
    print()
    print("minimum distance is :",dist[0])
else:
    print("no solution")
