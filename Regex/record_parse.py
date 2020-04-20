'''
Write a program to parse the given records and display in the given format



714016104004^AAA^#COIMBATORE^9876543213

714016104002^ABC^#MADRAS^9877543213

714016104003^XYC^9897543215

714016104003^#ERODE


Explanation:

Fields within the record are separated by '^'.
Each record is in one line.
Single student can have his details separated into multiple records and stored.If so display it as single record in output.
Any missing field must be displayed as "null" in output.
Output must be in the sorted order.


Constrains:

Regno^name^#city^mobile number

714016104004^AAA^#COIMBATORE^9876543213

Regno-Must always starts with '7'
Name-Can be of any length.
City-Starts with # and can be of any length
Mobile Number-It must be only a 10 digit number , starting with 7,8,9.
'''

dic = {}
for i in range(int(input())):
    temp = input().split('^')
    rollno = temp[0]
    dic.setdefault(rollno,['null','null','null'])
    for j in  temp[1:]:
        if '#' in j:
            dic[rollno][1] = j
        elif j.isdigit():
                if j[0] in ['7','8','9']:
                    dic[rollno][2] = j
        else:
            dic[rollno][0] = j
for i,j in sorted(dic.items(), key = lambda x : x[0]):
    print(i+' ','  '.join(j))
