'''
Year is 3030, water is a scare resource. civilizations live around glaciers in clusters, with a federal body
(identified as F) in center melting glaciers and controlling the water distribution. Each cluster has need
for water for a day and water for a day and a water storage capacity. Cluster are connected to each
other with a pipe identified by _ . pipes are flow controlled and water flows in forward direction only.
Every time water starts flowing through pipe. The clusters drain their tanks for use in other activities, as
they can use the water flowing to fill the tanks, and federal body sends water till the capacity is full.
Tanks are empty at beginning of day, water tanks fill in an instant. Clusters don’t share their water with
other clusters, but allow federal water to flow through the pipe. Federal body releases water at start of
day, clusters uses water at end of day. In a pipe link like F-C1--C2-C3-C4. When federal water body
targets C3, only C3 and nodes before it (here C1,C2,C3) can fill the tank, C4 can fill it only when its
targeted.
Calculate the minimum water needed to help the civilizations survive for n days.
Input is multiple. First line is the number of days to survive. Second line the number of clusters followed
by their definitions. Next Is the number of links in the system, followed by the link definitions.
Custer definition 
C1 100 300
Here
C1  - Cluster name
100 – daily water need
300 – storage capacity
Link definition
F_C1
F – is the federal source of pipe
C – Is the sink destination  of pipe (Cluster tank)

Input 
2
3
C1 100 300
C2 150 300
C3 100 100

Output
1100

Input  
3
4
C1 100 300
C2 100 300
C3 100 200
C4 100 400
4
F_C1
F_C2
C2_C3
C3_C4
Output
1700
'''


#import packages
from collections import OrderedDict as od

#initialization of variables
tank_info, tank_fill, connection , water_needed = od(), od(), [], 0

def getInput():
    #get tanks
    no_of_tanks = int(input())
    for _ in range(no_of_tanks):
        val = input().split()
        tank_info[val[0]], tank_fill[val[0]] = list(map(int,val[1:])), 0
       
    #path connection
    no_of_links = int(input())
    for _ in range(no_of_links):
        link = input().split('_')
        if 'F' == link[0]:
            connection.append([link[1]])
        else:
            for tank in connection:
                if link[0] in tank:
                    tank.append(link[1])
                   
def initialFill(connection):
    global water_needed
    for link in connection:
        for tank in link:
            water_needed+=tank_info[tank][1]
            tank_fill[tank]+=tank_info[tank][1]

def chekForDrained(drained_tank):
    for tank, storage in tank_fill.items():
                if storage < tank_info[tank][0]:
                    for temp in connection:
                        if tank in temp:
                            ind = connection.index(temp)
                            break
                    drained_tank[ind] = tank  

def refillTanks(drain):
    global water_needed
    for tanks in connection:
        if drain in tanks:
            for tank in tanks:
                tank_fill[tank] = tank_info[tank][1]
                water_needed += tank_info[tank][1]
                #Till target tank(drained tank)
                if tank == drain:
                    break
               
def useOfWater(no_of_days):
    global water_needed
    while True:
        for tank in tank_fill.keys():
            tank_fill[tank]-=tank_info[tank][0]
       
        #day decrement
        no_of_days-=1
       
        #exit loop when days ended
        if no_of_days==0:
            break
        else:
            #check for tank drained
            drained_tank = [0 for _ in range(len(connection))]
            chekForDrained(drained_tank)
           
            #refill drained tanks
            for drain in drained_tank:
                #check for drained tanks
                if drain:
                    refillTanks(drain)  
    return water_needed


   
if __name__=='__main__':
    #no of days
    no_of_days = int(input())
   
    #get input
    getInput()

    #fill tank at beginning of day
    initialFill(connection)
   
    #days iteration
    answer = useOfWater(no_of_days)

    #final answer
    print(answer)

'''
Input  
3
4
C1 100 300
C2 100 300
C3 100 200
C4 100 400
4
F_C1
F_C2
C2_C3
C3_C4
Output
1700

2
4
C1 200 400
C2 200 300
C3 100 100
C4 150 300
4
F_C1
F_C3
C1_C2
C3_C4
Output
1900

3
4
C1 200 300
C2 150 300
C3 200 200
C4 100 400
4
F_C1
F_C3
C3_C4
C1_C2
Output
2500
'''
