def fn(a):
    c1,c2=0,0
    for i in range(len(a)):
        if(a[i].isdigit()):
            for j in range(i+1,len(a)):
                if((a[j].isdigit())):
                    if(int(a[i])+int(a[j])==10):
                        c1+=1
                        if(a[i:j].count('?')==3):
                            c2+=1
                            break
    if c1==c2:
        return True
    else:
        return False


a="5??aaaaaaaaaaaaaaaaaaa?5?5"

if(fn(a)==True):
    print('True')
else:
    print("False")
    
'''
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and
check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false.
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5"
then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
'''

