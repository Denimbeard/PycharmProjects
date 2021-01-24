def mergesort(arr):
    step = 1
    print('Step: ',step, arr)
    if len(arr) < 2:
        return arr
    
    sortedList = []
    mid = int(len(arr) / 2)
    firstItem = mergesort(arr[:mid])
    secondItem = mergesort(arr[mid:])
    i = 0
    j = 0
    while i < len(firstItem) and j < len(secondItem):
        if firstItem[i] > secondItem[j]:
            sortedList.append(secondItem[j])
            j += 1
        else:
            sortedList.append(firstItem[i])
            i += 1
    sortedList += firstItem[i:]
    sortedList += secondItem[j:]
    step +=1
    return sortedList
