'''
Cricket Score
Design a cricket dashboard using the input string as the runs.
W - Wide
O - Out
. – Dot
1,2,3,4,6(runs)
P1…..P11=Player 1 to Player 11
----------------------------------------------------------------------------------------------------------
'''
#initialization
players=[['P1',0],['P2',0],['P3',0],['P4',0],['P5',0],
         ['P6',0],['P7',0],['P8',0],['P9',0],['P10',0],['P11',0]]
match,overs,balls,extras,count,played,i,j,total='',0,0,0,0,1,0,1,0
conditions=['W','O','.','1','2','3','4','6','.','0']
def get_input():
    global match
    match=input()
    
def calculate():
    global players,overs,balls,extras,count,played,i,j
    while(True):
        if(balls==6):
            overs+=1
            balls=0
            i,j=j,i        
        if(count==len(match) or played==11):
            break
        if(match[count] in conditions):
            if(match[count]=='W'):
                extras+=1
            elif(match[count]=='.'):
                balls+=1
            elif(match[count].isdigit()):
                balls+=1
                players[i][1]+=int(match[count])
                if(int(match[count])%2!=0 or int(match[count]==1)):
                    i,j=j,i
            elif(match[count]=='O'):
                i=(max(players.index(players[i]),players.index(players[j])))+1
                played+=1
                balls+=1
        count+=1
def result():
    global total,overs,balls,extras,count,played,i,j
    for m,n in players:
        if(int(players.index([m,n])<=played)):
            total+=n
            print(m,'-',str(n)+'(runs)')
    if(played<=10):
        print('Strike -',players[i][0])
    print('Non-Strike - '+players[j][0])
    print('Total-',extras+total)
    print('Overs -',overs+(balls/10))
    print('Extra -',extras)
    print('Wicket(s) -',played-1)
    print('Remaining Wickets(s) -',len(players)-played)

def main():
    
    get_input()
    calculate()
    result()
if __name__=='__main__':
    main()




"""
------------------------------------------------------------------------------------
WWW...23O11..46

P1 - 16(runs)
P2 - 0(runs)
P3 - 1(runs)
Strike - P3
Non-Strike - P1
Total- 20
Overs - 2.0
Extra - 3
Wicket(s) - 1
Remaining Wickets(s) - 9


46112W1O166O.21143O

P1 - 14(runs)
P2 - 13(runs)
P3 - 11(runs)
P4 - 1(runs)
P5 - 0(runs)
Strike - P3
Non-Strike - P5
Total- 40
Overs - 3.0
Extra - 1
Wicket(s) - 3
Remaining Wickets(s) - 7


...222431666

P1 - 7(runs)
P2 - 25(runs)
Strike - P1
Non-Strike - P2
Total- 32
Overs - 2.0
Extra - 0
Wicket(s) - 0
Remaining Wickets(s) - 10

"""








