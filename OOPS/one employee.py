class Employee:
    
    def __init__(s):
        s.emp_name=''
        s.emp_id=''
        s.designation=''
        s.salary=0
        s.level=''
        
    def getinput(s):
        s.emp_name=input('Empolyee name ')
        s.emp_id=input('Empolyee id ')
        s.designation=input('Employee designation ')
        s.salary=int(input('Employee salary '))
        
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
    def show(s):
        for i,j in s.__dict__.items():
            print(i,':',j)

def main():
    rag=Employee()
    rag.getinput()
    rag.allocate()
    rag.show()
    
if __name__=='__main__':
    main()
    



        
