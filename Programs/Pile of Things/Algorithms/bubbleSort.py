def bold(array, comp):
    newArray = []
    for element in array:
        if element == array[comp] or element == array[comp+1]:
            element = "**"+str(element)+"**"
            newArray.append(element)

        else: newArray.append(element)
    return newArray

def bubbleSort(arr): 
    step = 1
    n = len(arr)
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] < arr[j+1] :
                print('Step',step,':', str(bold(arr,j)).translate({39: None}), '| Comparisons = 1 Swaps = 0')
                arr[j+1], arr[j] = arr[j], arr[j+1] 
                step += 1
            else: 
                print('Step',step,':', str(bold(arr,j)).translate({39: None}), '| Comparisons = 1 Swaps = 1')
                step += 1
