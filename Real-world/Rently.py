import time
#from collections import Counter as cs

def find(i,temp,t):
    if(len(temp)==1):
        if(set(i.split()).issubset(set(temp[0].split()))):
            t.append(str(sentences.index(temp[0])))
            return
    if(set(i.split()).issubset(set(' '.join(temp[:(len(temp)//2)]).split()))):
        find(i,temp[:(len(temp)//2)],t)
    if(set(i.split()).issubset(set(' '.join(temp[(len(temp)//2):]).split()))):
        find(i,temp[(len(temp)//2):],t)
    return t

def textQueries(sentences, queries):
    start_time = time.time()
    if(1<=len(sentences)<=10**4 and 1<=len(queries)<=10**4):
        temp=' '.join(sentences).split()
        for i in queries:
            t=[]
            if(set(i.split()).issubset(set(temp))):
                t=find(i,sentences,t)                
                if(t!=[]): print(' '.join(t))
                else: print(-1)
            else:
                print(-1)
        del(t,sentences,queries,temp)       
    else:
        print(-1)
    end_time = time.time()
    print(end_time-start_time)

    
if __name__ == '__main__':
    sentences_count = int(input().strip())  

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    textQueries(sentences, queries)
'''
3
bob and alice like to text
bob does not like 
Alice like
3
bob alice
like
alice
'''


'''
linear search
#for j in sentences:
                    #if(set(i.split()).issubset(set(j.split()))):
                        #a=cs(j.split())
                        #z=[a[i] for i in i.split()]
                        #t.extend(str(sentences.index(j))*min(z))
                        #t.append(str(sentences.index(j)))

'''
