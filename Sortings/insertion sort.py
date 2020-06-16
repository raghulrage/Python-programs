lis = [7,3,2,9,4,5]

def insertionSort(lis):
    for i in range(1,len(lis)):
        key = lis[i]

        j = i-1
        
        while j>=0 and key<lis[j]:
            lis[j+1] = lis[j]
            j -= 1

        lis[j+1] = key

insertionSort(lis)

print(lis)
