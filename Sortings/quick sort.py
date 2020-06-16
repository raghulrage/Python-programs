lis = [7,3,2,9,4,5]

def partition(lis, low, high):

    i = low - 1
    #last element as pivot
    pivot = lis[high]

    #rearrangin list in order with pivot
    for j in range(low,high):
        
        if lis[j] <= pivot:
            i = i+1
            lis[i],lis[j] = lis[j], lis[i]

    lis[i+1], lis[high] = lis[high], lis[i+1]

    return i+1

def quickSort(lis,low,high):
    
    if low < high:
        
        #get partition element
        p = partition(lis, low, high)

        #sublist lessar than partition element
        quickSort(lis,low,p-1)
        
        #sublist greater than partition element
        quickSort(lis,p+1,high)
        
n = len(lis)

quickSort(lis, 0, n-1)

print(lis)
