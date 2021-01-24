def findValue(list):
    result = []
    i = 0
    length = len(list)
    while i < length:
        x = list[i]
        if x < 0:      
            result.append(i)
        i = i + 1 
    return result

print(findValue([-3,7,-4,3,2,-6]))
