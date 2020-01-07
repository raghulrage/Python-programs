num=int(input("No of entries"))
entry=[]
total_entry=[]
inside=0
insidelist=[]
insidetime=[]
outsidetime=[]
total_entry=[[1,3,'enter'],[2,2,'exit'],[3,6,'enter'],[4,1,'exit'],[5,2,'enter'],[6,8,'exit']]
'''for i in range(num):
    time=int(input("Enter timestamp"))
    ppl=int(input("Enter people"))
    path=input("Enter enter/exit")
    entry.extend([time,ppl,path])
    print(entry)
    total_entry.append(entry)
    entry=[]
    print("")
print(total_entry)'''
for i in range(num):
    if(total_entry[i][2]=="enter"):
        inside+=total_entry[i][1]
        timestamp=total_entry[i][0]
        insidetime.append(timestamp)
    else:
        insidelist.append(inside)
        timestamp=total_entry[i][0]
        outsidetime.append(timestamp)
        inside-=total_entry[i][1]
maximum=max(insidelist)
mx=insidelist.index(maximum)
print(insidelist[mx])
print(insidetime[mx])
print(outsidetime[mx])
