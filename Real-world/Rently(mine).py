
def textQueries(sentences, queries):
    start_time = time.time()
    temp=set(' '.join(sentences).split())
    for i in queries:
        s=set(i.split())
        if(s.issubset(temp)):
            t=tuple()
            for a,j in enumerate(sentences):
                if s.issubset(set(j.split())):
                    t+=(str(a),) 
            if t:
                print(' '.join(t))
            else:
                print(-1)
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



