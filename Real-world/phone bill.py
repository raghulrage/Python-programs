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

