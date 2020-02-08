'''school = {'Class_A':{'jeevan':{'English':80,'Maths':90,'Tamil':99},
        'sam':{'English':89,'Maths':90,'Tamil':100},
        'raghul':{'English':87,'Maths':100,'Tamil':66},
        'kishor':{'English':100,'Maths':90,'Tamil':55},
        'kutty':{'English':80,'Maths':55,'Tamil':77}
        },
        'Class_B':{'sankar':{'English':100,'Maths':90,'Tamil':62},
        'varsha':{'English':44,'Maths':90,'Tamil':44},
        'shruthi':{'English':80,'Maths':88,'Tamil':66},
        'sanjeev':{'English':80,'Maths':100,'Tamil':77},
        'hari':{'English':100,'Maths':90,'Tamil':89}
        },
        'Class_C':{'gowtham':{'English':80,'Maths':90,'Tamil':100},
        'swathi':{'English':73,'Maths':88,'Tamil':65},
        'deepki':{'English':68,'Maths':100,'Tamil':79},
        'latha':{'English':90,'Maths':90,'Tamil':90},
        'raja':{'English':100,'Maths':100,'Tamil':100}
        }
        }
'''
school=dict()
sub=['Eng','Tam','Mat','Sci']
for i in range(int(input('Enter no. of classes: '))):
    n=input('\nEnter class name: ')
    school.setdefault(n)
    stu=dict()
    s=dict()
    for i in range(int(input('Enter no. of students'))):       
        s.setdefault(input())
        print(school,s)
        school[n]=stu
        
print(school)
