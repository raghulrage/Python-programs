def CorrectPath(s): 
    res=""
    d=s.count("d")-s.count("u")
    r=s.count("r")-s.count('l')
    for i in s:
        if i=="?":
            if d<4:
                res=res+"d"
                d=d+1
            elif d>4:
                res=res+"u"
                d=d-1
            elif r<4:
                res=res+"r"
                r=r+1
            elif r>4:
                res=res+"l"
                r=r-1
        else:
            res=res+i
    return res

print (CorrectPath("rd?u??dld?ddrr"))

'''
Have the function CorrectPath(str) read the str parameter being passed,
which will represent the movements made in a 5x5 grid of cells starting from the top left position. 
The characters in the input string will be entirely composed of: r, l, u, d, ?. 
Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down.
Your goal is to determine what characters the question marks should be in order for a path to be created to go from
the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid.

For example: if str is "r?d?drdd" then your program should output the final correct string
that will allow a path to be formed from the top left of a 5x5 grid to the bottom right.
For this input, your program should therefore return the string rrdrdrdd. 
There will only ever be one correct path and there will always be at least one question mark within the input string.
Examples
Input: "???rrurdr?"
Output: dddrrurdrd
Input: "drdr??rrddd?"
Output: drdruurrdddd
'''
