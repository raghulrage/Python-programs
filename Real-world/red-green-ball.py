'''
Red Green ball:
Red and Green Balls You have a square grid (NxN). Each cell of the grid has either a red ball or
a green ball. Your job is to arrange the balls in such a way that all the red balls are either on or
below the main diagonal. The main diagonal starts from cell 1x1 and ends at cell NxN. You have
only one move which is to swap adjacent rows. You need to achieve the final arrangement in
minimal number of moves. If it is not possible to come to a resolution by swapping then print -1
Input:
First line of input is the number of rows in grid. Rest are the lines in the grid
Output:
Minimum number of moves
-----------------------------------------------------------------------------------------------------
'''
#global initialization
box,count=[],0
def get_input():
    rc=int(input())
    for i in range(rc):
        box.append(list(input()))    
    return rc,box

def fact(rc):
    fact=0
    for i in range(1,rc):
        fact=fact+i
    return fact

def calculate(rc,box,fact):    
    while(True):
        global count
        temp=0
        #check condition whether there is not 'R' in top of diagonals 
        for i in range(rc):
            for j in range(rc):
                if(j>i):
                    if(box[i][j]!='R'):
                        temp+=1

        #if no 'R' present break the loop
        if(temp==fact):
            break
        
        for i in range(len(box)-1):
            if('R' in box[i] and 'R' in box[i+1]):
                    if(box[i][::-1].index('R')<box[i+1][::-1].index('R')):
                        box[i][::-1],box[i+1][::-1]=box[i+1][::-1],box[i][::-1]
                        count+=1
                        break
            elif('R' not in box[i+1]):
                box[i][::-1],box[i+1][::-1]=box[i+1][::-1],box[i][::-1]
                count+=1
                break
        else:
            break
    return box,count

def check(rc,count):
    for i in range(rc):
        for j in range(rc):
            if(j>i):
                if(box[i][j]=='R'):
                    return -1          
    return count

def main():
    rc,box=get_input()
    factorial=fact(rc)
    box,count=calculate(rc,box,factorial)
    count=check(rc,count)
    print(count)
    


if __name__=='__main__':
    main()

    
"""

5
GRGGG
RGRRG
RGGGG
GRRRG
GGRGG
4



2
GR
RG
1



7
GGRRRGG
RRRGGGG
RRGGRGG
GGGGGGG
RRGGGGG
GGGGGRG
RGGGGGG
10

10
RRRRRRRRRR
RRRRRRRRRG
RRRRRRRRGG
RRRRRRRGGG
RRRRRRGGGG
RRRRRGGGGG
RRRRGGGGGG
RRRGGGGGGG
RRGGGGGGGG
RGGGGGGGGG
45
"""
            

