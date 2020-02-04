
def textQueries(sentences, queries):
    # 1. build the hash map
    start_time = time.time()
    word_map = {}
    for query in queries:
        for query_word in query.split():        
            for i, sentence in enumerate(sentences):
                if query_word in sentence:
                    word_map.setdefault(query_word, []).append(i)
    for query in queries:
        # 2. look up in the hash map
        final_set = set()
        for word in query.split():
            if not final_set:
                final_set = set(word_map.get(word, []))
            else:
                final_set = final_set.intersection(word_map.get(word, []))
            if not final_set:
                break
        # 3. print the indices
        if final_set:
            print(' '.join( str(i) for i in sorted(final_set)))
            # or
            #print(*sorted(final_set), sep=' ')
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
def testQueries(sentences,queries):
    words={}
    for qs in queries:
        for q in qs.split():
            for i,s in enumerate(sentences):
                if q in s:
                    words.setdefault(q,[]).append(i)
    for qs in queries:
        ans=set()
        for q in qs.split():
            if not ans:
                ans=set(words[q])
            else:
                ans=ans.intersection(words[q])
            if not ans:
                break
        if ans:
            print(' '.join(str(i) for i in sorted(ans)))
        else:
            print(-1)
if __name__=='__main__':
    sentences=['i like you','i love you','i like love']
    queries=['like','love','like love']
    testQueries(sentences,queries)
'''
