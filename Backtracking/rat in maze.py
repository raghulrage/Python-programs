    
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
