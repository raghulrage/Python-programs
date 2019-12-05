#----------------------------------------PRODUCT MANAGEMENT----------------------------------------------

#INSERT A PRODUCT
def insert():
        item_id=int(input())
        item_name=input()
        quantity=int(input())
        price=int(input())
        exp_data=input()
        manf_date=input()
        product=[item_id,item_name,quantity,price,exp_data,manf_date]
        item.append(product)


#UPDATE A PRODUCT        
def update():
    up_id=int(input())
    for i in item:
        if(up_id==i[0]):
            j=item.index(i)
            item.pop(j)
            item_name=input()
            quantity=int(input())
            price=int(input())
            exp_data=input()
            manf_date=input()
            product=[up_id,item_name,quantity,price,exp_data,manf_date]
            item.insert(j,product)
            print(item)


#DELETE A PRODUCT
def delete():
    del_id=int(input())
    for i in item:
        if(del_id==i[0]):
            j=item.index(i)
            item.pop(j)


#SEARCH A PRODUCT
def search():
    search_id=int(input("enter an id to search",))
    for i in item:
        if(i[0]==search_id):
            print("{} {} {} {} {} {}".format(i[0],i[1],i[2],i[3],i[4],i[5]))


#VIEW ALL PRODUCTS
def view():
    for i in range(len(item)):
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(item[i][0],item[i][1],item[i][2],item[i][3],item[i][4],item[i][5]))



        
#DRIVER CLASS
        
item=[['ID','NAME','QTY','PRICE','EXPY','MAFX']]  
while(1):
    print("enter 1.Insert 2.Update 3.Delete 4.Search 5.View 6.Exit")
    op=int(input())
    if(op==1):
        insert()
    elif(op==2):
        update()
    elif(op==3):
        delete()
    elif(op==4):
        search()
    elif(op==5):
        view()
    elif(op==6):
        break
