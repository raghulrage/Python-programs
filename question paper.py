print("*************\nWelcome to Python Quiz*************")
start=int(input("Enter 1 to start quiz"))
if(start==1):
    qns=["Author of Python","Which function is used to display a user content","Which function is used to get data from user"]
    opts=[["GVR","Steve Jobs","J G","P N"],["print()","input()","format()","eval()"],["print()","input()","format()","eval()"]]
    answer=[opts[0][0],opts[1][0],opts[2][1]]
    mark=[0,0,0]
    i=0
    while(i<3):
        print("your Question Q{}\n".format(i+1))
        print("Description {}\n".format(qns[i]))       
        print("Options {}\n".format(opts[i]))
        ans=input("typer your answer")
        if(ans==answer[i]):
            mark[i]=1
        else:
            mark[i]=0
        nxt=int(input("Select your options\n1.Next\n2.Previous"))
        if(nxt==1):
            i+=1
        elif(i>0):
            i-=1
    print("YOUR score",sum(mark),'out of 3')
