
def purchase():
    global total
    num=int(input())
    for i in range(num):
        name=input()
        quantity=int(input())
        price=int(input())
        product=[name,quantity,price,quantity*price]
        item.append(product)
        total+=quantity*price

        

def view():
    col=["S.no",'name','product','price','total price']
    print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(col[0],col[1],col[2],col[3],col[4]))
    for i in range(len(item)):
        print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(i+1,item[i][0],item[i][1],item[i][2],item[i][3]))

def bill():
    print("Total amount",total)
    print("discount",end='')
    if(total<=500):
        discount=total*2/100
    elif(500<total<=1000):
        discount=total*5/100
    elif(total>1000):
        discount=total*8/100
    print(discount)
    print("Amount Payable",total-discount)

    
item=[]
total=0
while(1):
    opt=int(input("1.To purchase 2.view items 3.Generate Bill 4.exit"))
    if(opt==1):
        purchase()
    if(opt==2):
        view()
    if(opt==3):
        bill()
    if(opt==4):
        break
