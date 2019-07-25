num=int(input())
temp=num
dh=temp//10
dl=temp%10
dsum=dh+dl
dmul=dh*dl
dnum=dsum+dmul
if(num==dnum):
    print("special")
else:
    print("Not special")
