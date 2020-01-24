#Ajira Technologies
#Problem Statement
"""
Mesoketes
You are watching the battle of Mesoketes, that had a big wall that covered the city on all
sides. The wall was built by the Maygans to protect against military incursions from the
North. For the purposes of this problem, the wall is a square. We assume that the builder used
a reactive strategy: whenever a side of the wall was attacked successfully, the Wall on that
side would be raised to the height sufficient to stop an identical attack in the future.
The north wall of Mesoketes was frequently attacked by nomadic tribes. For the purposes of
this problem, we assume that each tribe attacks the wall with some weapon X, strength S (the
strength defines the height at impact) and in a direction (N,S,E,W). The weapon has a
magnitude of 1 and it is the strength that defines the attack. In order to repel the attack, the
Wall must have height S all along the defended side of the wall. If the height on that side of
the Wall is lower than needed, the attack will breach the Wall at this point and succeed. Note
that even a successful attack does not damage the Wall. After the attack, every attacked
fragment of the Wall that was lower than S is raised to height S — in other words, the Wall is
increased in the minimal way that would have stopped the attack. Note that if two or more
attacks happened on the exact same day, the Wall was raised only after they all resolved, and
is raised in the minimum way that would stop all of them.
Assuming that initially (in 250 BC) the Wall was nonexistent (i.e., of height zero
everywhere), and given the full description of all the nomadic tribes that attacked the Wall,
determine how many of the attacks were successful. Weaponry has not advanced across the
globe and thus all tribes have the same weapon X
"""
import copy
#initialization
wall,attack,count={'N':0,'W':0,'E':0,'S':0},[],0

def get_input():
    n=input().split(';')
    for i in n:
        if(':' in i):
            temp_list=[]
            temp=i.split(':')
            for i in temp:
                temp_list.append(spliting(i))
            attack.append(temp_list)
        else:
            attack.append([spliting(i)])  
def spliting(i):
    a=[]
    for k in i[::-1]:
        if(k.isdigit()):
            a.append(int(k))
        if(k in wall):
            a.append(k)
            break
    return a 
    
def find_val():
    for k in attack:
        temp_wall=copy.deepcopy(wall)
        for i,j in k:
            global count
            if(wall[j]<i):
                temp_wall[j]=i
                count+=1
        for i in wall.keys():
            if(wall[i]<temp_wall[i]):
                wall[i]=temp_wall[i]                
    return count
        
def main():
    get_input()
    print(find_val())
    
if __name__=="__main__":
    main()
    
"""
Input
Day 1$ T1 - E - X - 4; Day 2$ T1 - W - X - 3 : T2 - E - X - 3; Day 3$ T3 - N - X - 2: T2 - W - X - 4
Output
4

Input 
Day 1$ T1 - N - X - 3: T2 - S - X - 4: T3 - W - X - 2; Day 2$ T1 - E - X -4: T2 - N - X - 3: T3 - S - X - 2; Day 3$ T1 - W - X - 3: T2 - E - X - 5:T3 - N - X - 2
Output
6

Input
Day 1$ T1 - N - X - 5 : T2 - W - X - 3;Day 2$ T1 - S - X - 2
Output
3

Input
Day 1$ T1 - W - X - 4; Day 2$ T2 - W - X - 3
Output
1

Input
Day 1$ T1 - E - X - 4; Day 2$ T1 - W - X - 3
Output
2

Input
Day 1$ T1 - E - X - 4; Day 2$ T1 - W - X - 3 : T2 - E - X - 3
Output
2
Input
Day 1$ T1 - S - X - 4: T1 - N - X - 2: T3 - W - X - 3; Day 2$ T2 - S - X -5: T2 - N - X - 1: T3 - N - X - 3; Day 3$ T1 - W - X - 2: T1 - W - X - 4:T2 - N - X - 3: T2 - S - X - 4
Output
6
"""
