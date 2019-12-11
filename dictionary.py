from functools import reduce
def average():
    '''avg=0
    for i in d.values():
        avg+=i['Eng']
    print(avg//len(d))'''
    print(reduce(lambda x,y:x+y,d.values()['Eng']))

def highest():
    '''
    l=[]
    for k,v in d.items():
        l.append([v['Eng'],k])
    print(max(l))
    '''
    sub=input("Enter subject to get highest scored student based on it\n")
    print(sorted(d.items(), key=lambda x:x[1][sub],reverse=True)[0][0])

def mark():
    '''
    l=[]
    for k,v in d.items():
        l.append([v['Eng'],k])
    print(sorted(l))
    '''
    sub=input("Enter subject to sort based on it")
    print([[i[0],sub,i[1][sub]] for i in (sorted(d.items(), key=lambda x:x[1][sub],reverse=True))])
#
def total():
    name=input("Enter student name to get total")
    total=0
    for k,v in d[name].items():
        total+=v
    print(total)

def passed():
    sub=input("Enter subject to get passed students")
    print=list((filter(lambda x:x[1]>50,[[k,v[sub]]  for k,v in d.items()])))



#driver class 
d={
   'Raghul':{'Eng':80,'Mat':40},
   'Rupesh':{'Eng':70,'Mat':60},
   'Jeevan':{'Eng':34,'Mat':70},
   'Sam':{'Eng':82,'Mat':40}
  }
while(1):
    option=int(input("\n1.Average 2.High score 3.Sort 4.total of a student 5.Students passed 6.Exit\n"))
    if(option==1):
        average()
    elif(option==2):
        highest()
    elif(option==3):
        mark()
    elif(option==4):
        total()
    elif(option==5):
        passed()
    else:
        break
