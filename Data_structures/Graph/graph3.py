def ladderLength(beginWord,endWord,wordList):
        q=[(beginWord,1)]
        for word,d in q:
            if word==endWord:
                return d+1
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    tmp=word[:i]+char+word[i+1:]
                    if tmp in wordList:
                        q.append([tmp,d+1])
                        wordList.remove(tmp)
        return 0

start = input()
l = [input() for i in range(int(input()))]
end = input()
print('',ladderLength(start,end,l))