n=int(input())

l=n*2-1

for i in range(l):
    
    for j in range(l):
        
        a=min( i , j , l-j-1 , l-i-1 )
        
        print(n-a,end=' ')
        
    print()
