"""
"""
2.Electricity Bill Calculation

The consolidated power consumption for a commercial complex is sent in the following
format by EB department for a month. The complex has 5 shops each having a separate
meter box and the electricity tariff total for a month has to be calculated for each shop
separately based on the number of units consumed.
NOTE: The same shop may have more than one entry in a single line. Sometimes if a
shop does not
consume energy it will not be part of the list. On power shutdown days the entry will be
nothing just the date
Find the total power consumed if each shop is charged in the following slabs
First 999 units: 0.40/unit
1000-2000 units: 0.33/unit
2001-5000 units: 0.30/unit
5000+units: 0.20/unit
--------------------------------------------------------------------------------------------------------------
"""

#initialization
shop={}

def cal(lis):
    for i,j in lis:
        if(j<=999):
            k=j*0.40
        elif(1000<=j<=2000):
            k=j*0.33
        elif(2001<=j<=5000):
            k=j*0.30
        elif(j>5000):
            k=j*0.20         
        print("{}:{:.2f}".format(i,k))
        
def get_input():
    for i in range(int(input())):
        val=input().split('$')
        val[0]=''.join(val[0].split(':')[1:]).strip()
        val=[i.split() for i in val]
        for i in val:
            if i!=[]:
                if i[0] not in shop.keys():
                    shop[i[0]]=int(i[1])
                else:
                    shop[i[0]]+=int(i[1])
def main():
    get_input()
    shop_list=sorted(shop.items() , key=lambda x:x[0])
    cal(shop_list)
    
if __name__=='__main__':
    main()


"""
8
Jan 1, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 5
Jan 2, 2020: shop5 318$shop4 320$shop3 330$shop2 420$shop1 5
Jan 3, 2020: shop1 316$shop1 820$shop3 330$shop4 420$shop5 5
Jan 4, 2020: shop1 314$shop2 110$shop3 68$shop4 420$shop5 5
Jan 5, 2020: shop1 323$shop2 220$shop3 330$shop4 420$shop5 5
Jan 6, 2020: shop1 324$shop3 330$shop4 420$shop5 5
Jan 7, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 51
Jan 8, 2020:
output
shop1:822.60
shop2:392.70
shop3:614.40
shop4:852.00
shop5:157.60

6
Jan 01, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 57
Jan 02, 2020: shop5 81$shop4 380$shop3 327$shop2 240$shop1 318
Jan 03, 2020: shop1 316$shop3 334$shop4 400$shop5 75$shop2 211
Jan 04, 2020:
Jan 05, 2020: shop1 323$shop2 210$shop3 300$shop4 418$shop5 43
Jan 06, 2020: shop1 324$shop3 315$shop4 411$shop5 48

shop1:528.33
shop2:352.40
shop3:529.98
shop4:608.70
shop5:121.60
"""
