print("*************\nWelcome to Python Quiz*************")
start=int(input("Enter 1 to start quiz"))
if(start==1):
    qns=["Author of Python","Which function is used to display a user content","Which function is used to get data from user"]
    opts=[["GVR","Steve Jobs","J G","P N"],["print()","input()","format()","eval()"],["print()","input()","format()","eval()"]]
    answer=["GVR","print()","input()"]
    i=0
    mark=0
    while(i<3 and i>=0):
        print("your Question Q{}\n".format(i+1))
        print("Description {}\n".format(qns[i]))       
        print("Options {}\n".format(opts[i]))
        ans=input("typer your answer")
        if(ans==answer[i]):
            mark+=1
            print(mark)
        else:
            if(mark>0):
                mark-=1
                print(mark)
        nxt=int(input("Select your options\n1.Next\n2.Previous"))

        if(nxt==1):
            i+=1
        else:
            i-=1
        
