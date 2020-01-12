l=[[3,4],[1,2,7,7]]
l=[[13,4],[1, 2, 3, 6, 14]]
l=[[5,9],[1, 2, 6, 7]]
m=max(l[0])
n=min(l[0])
d=m-n
l2,l3,l4,l5=l[1],[],[],[]
for i in range(len(l2)-1):
    if(l2[i]+l2[i+1]==d):
        l3.append([l2[i],l2[i+1]])
if(l3==[]):
    for i in l2:
        l4.append(l[0][0]+i)
        l5.append(l[0][1]+i)
    for i in range(len(l4)):
        if(l4[i] in l5):
            s=[l[1][l4.index(l4[i])],l[1][l5.index(l4[i])]]
            if(d is min(s)):
                print(d)
            else:
                print(s)
            break
    else:
        print ('No')
else:
    print(l3[0])
                
'''Have the function ScaleBalancing(strArr) read strArr which will contain two elements,
the first being the two positive integer weights on a balance scale (left and right sides) and
the second element being a list of available weights as positive integers. 
Your goal is to determine if you can balance the scale by using the least amount of weights from the list,
but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] 
then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. 
It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and
adding a 2 to the right side. Both scales will now equal 11 and they are perfectly balanced.
Your program should return a comma separated string of the weights that were used from the list in ascending order,
so for this example your program should return the string 2,6

There will only ever be one unique solution and the list of available weights will not be empty.
It is also possible to add two weights to only one side of the scale to balance it.
If it is not possible to balance the scale then your program should return the string not possible.
Examples
Input: ["[3, 4]", "[1, 2, 7, 7]"]
Output: 1
Input: ["[13, 4]", "[1, 2, 3, 6, 14]"]
Output: 3,6
'''
