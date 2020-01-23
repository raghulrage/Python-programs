CHEMIST QUESTION

You have been hired as a software consultant at a chemist. The chemist shop sells various types of
compounds and mixture to their customers. They have a research team that put together various formulas
for the chemist of sell. The owner of the shop is a bit of stickler for cleanliness and is also afraid of
unforeseen reactions when creating the compounds. So,she has created a rule where a new mixing can is to
used for creating a new compound (whether the compound is made of the base elements or from another
set of pre-made compounds). Your job as a consultant is to determine the minimal number of bowls that
are required to make them. Any compound/element that is part of a definition, without its own definition
can be assumed to be a base element. base elements don’t need any preparation.

Multiline input. Where first line N specifies the number of compound definitions followed by N definitions.
Followed. Followed by integer M specifies the number of compounds to prepare and M compounds
to prepare.

Calculate the minimum number of bowls required to prepared the given compounds.
Test cases are followed by the code

------------------------------------------_________CODE_________------------------------------------------------------

#initialization
raw_components,component_to_prepare,count_value={},[],0

def get_input():
    global component_to_prepare
    for i in range(int(input())):
        input_raw_component=input().split('=')
        raw_components[input_raw_component[0].strip()]=[i.strip() for i in input_raw_component[1].split('+')]
    for i in range(int(input())):
        component_to_prepare.append(input())
    component_to_prepare=list(set(component_to_prepare))
    
def fn(n):
    temporary_component=[]
    global count_value
    for i in n:
        if(i in raw_components.keys()):
            count_value+=1
            temporary_component=raw_components[i]           
    if(temporary_component!=[]):
        fn(temporary_component)
    return count_value

def main():
    get_input()
    for i in component_to_prepare:    
        total_bowl=fn([i])
    print(total_bowl)

if __name__=="__main__":
    main()
  
------------------------------------------_____TEST-CASE______---------------------------------------------------------

Test case 1

Input
2
H2O = H + O
NaCL= Na + CL
1
NaCL
Output
1

Test case 2

Input 
2
H2O = H + O
NaCL= Na + CL
2
NaCL
NaCL
Output

1
Test case 3
Input 
4
H2O = H + O
NaCL = Na + CL
H2SO4 = H2O + S03
S03 = S + O
1
H2SO4

Output
3
