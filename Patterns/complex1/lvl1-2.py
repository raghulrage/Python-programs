n=int(input())   
for i in range(0,n):    
    for j in range(0,n):     
        if (j == 1 or ((i == 0 or i == n//2 or i == n-1) and (j <n-2 and j > 1)) or (j == n-2 and (i != 0 and i != n//2 and i != n-1))) :  
            print(end='*')    
        else:      
            print(end=' ')    
    print()    

