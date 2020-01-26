'''
16. Write a program to calculate monthly phone bill	
Your rnonthly phone bill has just arrived, and it's unexpectedly large. 

You decide to verify the amount by recalculating the bill based on your phone call logs and the phone company's charges. 
The logs are given as a string S consisting of N lines separated by end-of-line characters (ASCII code 10). 
Each line describes one phone call using the following format 
""hh:mm:ss, nnn-nnn-nnn""
where ""hh:mm: ss"" denotes the duration of the call (in ""hh"" hours, ""mm"" minutes and ,""ss"" seconds) and ""nnn-nnn-nnn"" denotes the 9-digit phone number of the recipient (with no leading zeros). 

Each call is billed separately. The billing rules are as follows: 
• If the call was shorter than 5 minutes, then you pay 3 cents for every started second of the call (e.g. for duration ""00:01:07"" you pay 67*3 = 201 cents). 
• If the call was at least 5 minutes long, then you pay 150 cents for every started minute of the call (e.g. for duration ""00:05:00"" you pay 5* 150 = 750 cents and for duration ""00:05:01"" you pay 6 *150 = 900 cents). 
• All calls to the phone number that has the longest total duration of calls are free. In the case of a tie, if more than one phone number shares the longest total duration, the promotion is applied only to the phone number whose numerical value is the smallest among these phone numbers. 

Write a function: 

class Solution { public int solution(String 3); }

that, given a string S describing phone call logs, returns the amountof money you have to pay in cents.
 
For example, given string S with N = 3 lines: 

"00:01:07,400-234-090s
00:05:01,701-080-080
00:05:00,400-234-090" 

the function should return 900 (the total duration for number 400-234-090 is 6 minutes 7 seconds, and the total duration for number 701-080-080 is 5 minutes 1 second; therefore, the free promotion applies to the former phone number). 

Assume that 
• N is an integer within the range 1...100]; 
• every phone number follows the format ""nnn-nnn-nnn"" strictly; there are no leading zeros; • the duration of every call follows the format ""hh:mm:ss"" strictly (00 <= hh <= 99, 00 <= mm, ss <= 59); 
• each line follows the format ""hh:mm:ss,nnn-nnn-nnn "" strictly; there are no empty lines and spaces. 

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''



#solution 1 (old)

# Get_no_of_logs
num = int(input())

# list_initialization
duration, ph_num, log, bill = [], [], [], []

# Get_input
for i in range(num):
    val = input()
    temp = val.split(',')
    duration.append(temp[0])
    ph_num.append(temp[1])
    list_temp = duration[i].split(':')
    list_temp = list(map(int, list_temp))
    duration[i] = list_temp

# seperate_timestamp
for i in range(num):
    mint = duration[i][1]
    sec = duration[i][2]
    # duration above 5 mins
    if ((mint >= 5)):
        if (sec > 0):
            mint += 1
            temp = mint * 150
            bill.append(temp)
            
        else:
            temp = mint * 150
            bill.append(temp)
    # duration below 5 mins
    else:
        temp = mint * 60
        val = temp + sec
        val=val*3
        bill.append(val)

# Display_value
print()
for i in range(num):
    print(ph_num[i], '= Cents.', bill[i], ', Duration=', duration[i][1], ':', duration[i][2])

"""
00:02:45,890-765-566
00:05:23,236-418-785
00:07:00,236-418-785
"""

#solution 2

#initialization
d,d1,m,final={},{},{},[]

def getinput():
    n=input().split()
    for i in n:
        val=i.split(',')
        if(val[1] not in d):
            d[val[1]]=[list(map(int,val[0].split(':')))]
        else:
            d[val[1]].append(list(map(int,val[0].split(':'))))

def find_amount():
    for i in d.keys():    
        d1[i],val=[],0
        for j in d[i]:
            dur,hr,mins,sec=0,j[0],j[1],j[2]
            val+=(mins*60)+sec
            if(hr!=0):
                mins+=hr*60
            if(mins<5):
                dur+=(mins*60)+sec
                dur*=3
            else:
                if(sec>0):
                    mins+=1
                dur=mins*150
            d1[i].append(dur)
        d1[i]=sum(d1[i])
        m[i]=val
        
def total_amount():
        for i,j in sorted(m.items(),key=lambda x:x[1]):
            if(j==max(m.values())):
                final.append(i)
        final.sort()
        d1[final[0]]=0
        
def main():
    getinput()
    find_amount()
    total_amount()
    print('\n',sum(d1.values()))

if __name__=="__main__":
    main()
        
    
    
 
"""
00:02:45,890-765-566 00:05:23,236-418-785 00:07:00,236-418-78500:02:45,890-765-566 00:05:23,236-418-785 00:07:00,236-418-785
"""
"""
00:05:17,959-720-018 00:03:00,959-720-018 00:04:59,959-720-018
"""
"""
00:04:59,959-720-018 00:05:00,750-222-197 00:15:31,892-545-277
00:05:59,959-720-018 00:07:00,750-222-197 00:05:59,892-545-277
"""
"""
00:5:17,959-720-018 00:19:38,750-222-197 00:14:21,959-720-018 00:17:01,892-545-277
"""

