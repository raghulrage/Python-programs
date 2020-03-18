#import packages
import time
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
    for tank in connection:
        if drain in tank:
            for l in tank:
                if l!=drain:
                    tank_fill[l] = tank_info[l][1]
                    water_needed+=tank_info[l][1]
                else:
                    tank_fill[l] = tank_info[l][1]
                    water_needed+=tank_info[l][1]
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
   
    #fill tank at beginneing of day
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

'''
