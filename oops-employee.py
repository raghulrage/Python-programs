class Employee:

    # atributes initialization to an object
    def __init__(s):
        s.emp_name=''
        s.emp_id=''
        s.designation=''
        s.salary=0
        s.level=''

    #function to get input    
    def getinput(s):
        s.emp_name=input('Empolyee name ')
        s.emp_id=input('Empolyee id ')
        s.designation=input('Employee designation ')
        s.salary=int(input('Employee salary '))

    #function to allocate level
    def allocate(s):
        print()
        if(s.salary>=25000):
            s.level='A'
        elif(20000<=s.salary<25000):
            s.level='B'
        elif(15000<=s.salary<15000):
            s.level='C'
        else:
            s.level='D'
            
    #function to show object details        
    def show(s):
        for i,j in s.__dict__.items():
            print(i,':',j)
        print()
        
def maximum_salary(emp):
    
    max_sal=0
    
    for i in range(len(emp)):
        
        if(emp[i].salary>max_sal):
            
            max_sal=emp[i].salary
            employee=emp[i].emp_name
            des=emp[i].designation
            
    return max_sal,employee,des
        
def main():
    #emp=['emp'+str(i) for i in range(int(input('Enter number of employees: ')))]
    
    emp=[]

    #Get no of objects
    n=int(input('Enter number of employees: '))

    #Creation of objects and perform methods(get input & allocate levels)
    for i in range(n):
        
        emp.append('emp'+str(i))
        print('\nEnter Employee {} details\n'.format(i+1))
        emp[i]=Employee()
        emp[i].getinput()
        emp[i].allocate()

    #Display all object details
    for i in range(len(emp)):
        emp[i].show()
        
    #find maximum salary
    max_sal,employee,des=maximum_salary(emp)               
    print('\n',employee,'gets maximum salary of',max_sal,'Rupees, He is',des,'of our company')

if __name__=='__main__':
    main()
    
    



        
