class stud:
    def __init__(s,name):
        s.name=name
    def display(s):
        print('Hi',s.name)
    def __del__(s):
        print('Deleting')
obj=stud('Raghul')
obj.display()
print(obj)
del obj
print(obj)

        
