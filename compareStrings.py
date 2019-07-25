str1=input()
str2=input()
if(len(str1)<50 and len(str2)<50):
    if(str1==str2):
        print("Strings are equal")
    else:
        print("Strings are not equal")
else:
    print("String exceeds to 50 characters")
