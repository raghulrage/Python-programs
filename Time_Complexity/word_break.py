'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given

s = "snakesandladder",

dict = ["snake", "snakes", "and", "sand", "ladder"].

A solution is ["snakes and ladder", "snake sand ladder"].

Input Format
The first line contains an integer T, denoting the number of test cases.

Every test case has 3 lines.

The first line contains an integer N, number of words in the dictionary.

The second line contains N strings denoting the words of the dictionary.

The third line contains a string s.

Output Format
For each test case, print all possible strings.


Testcase 1 Input

1
5
snake snakes and sand ladder
snakesandladder

Testcase 1 Output
snake sand ladder
snakes and ladder

'''


import collections
def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    res = collections.defaultdict(list)
    res[0] = [[""]]        

    def dfs(i):
        if i<0:
            return
        else:
            for w in wordDict:
                if s[i-len(w):i]==w:
                    if i-len(w) not in res:
                        dfs(i-len(w))
                    for prefix in res[i-len(w)]:
                        res[i].append(prefix+[w])

    dfs(len(s))
    return [" ".join(words[1:]) for words in res[len(s)]]

for i in range(int(input())):
    n = input()
    dic = input().split()
    s= input()
    for i in wordBreak(s,dic)[::-1]:
        print(i)
