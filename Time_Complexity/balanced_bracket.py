'''
Consider a string consisting of the characters < and > only. We consider the string to be balanced if each < always appears before (i.e, to the left of) a corresponding > character (they do not need to be adjacent).Moreover, each < and > act as a unique pair of symbols and neither symbol can be considered as part of any other pair of symbols.

To balance a string, we can replace any > character with <>.Given an expression and a maximum number of replacements, can you turn an unbalanced string into a balanced one?

For example, the strings <<>>, <> , and <><> are all balanced, but the strings >>, <<>, and ><>< are unbalanced. The string >> can be balanced in two moves by replacing each > with a <> to make <><>.

FUNCTION DESCRIPTION:

Complete the function balancedOrNot in theeditor below. The function must return an array of integers where element[i] contains a 1 if expression[i] is balanced ora 0 if it is not.

balancedOrNot has the following parameter(s):

expression[expression[0]...expression[n-1]]: an array of strings to check

maxReplacements[maxreplacements[0],...maxReplacements[n-1]]:an array of integers representing the maximum number of replacements available for each expressions[i]

Input Format
The first line contains an integer n, the size of the array expressions.

The next n lines each contain an element expressions[i].

The next line contains an integer n, the size of the array maxReplacements

The next n lines each contain an element maxReplacements[i]

Output Format
Print either 1 if the string is already balanced.

or 1 if the string is balanced after replacement and the number of replacements is less than the maxReplacements.

else Print 0 for each test cases.

Constraints
• 1 <= n <= 102

• 1 <= length of expression[i] <= 105

• 0 <= maxReplacement[i] <= 105

Testcase 1 Input
2
<>>>
<>>>>
2
2
2

Testcase 1 Output
1
0

'''


def balancedOrNot(expressions, maxReplacements):
    return_array = []
    for i in range(0, len(maxReplacements)):
        return_array.append(0)

    for count, each_data in enumerate(expressions):
        check_str = expressions[count]
        replacement_count = 0
    
        continue_loop = True
        while len(check_str) >= 1 and continue_loop:
            opening_count = check_str.count('<')
            closing_count = check_str.count('>')
            
            if opening_count > closing_count:
                replacement_count = maxReplacements[count] + 1
                continue_loop = False
            elif check_str[0] == '>':
                replacement_count += 1
                check_str = check_str[1:]
            else:
                check_str = check_str.replace('<>','')

        if replacement_count <= maxReplacements[count]:
            return_array[count] = 1

    return return_array

s=[input() for i in range(int(input()))]
l = [int(input()) for i in range(int(input()))]
print(balancedOrNot(expressions = s, maxReplacements=l))
