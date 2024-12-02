f = open("Day2\day2.txt", "r")

safe = False
safeAmount = 0
isAscending = False
isDecending = False

def checkIfSafe(array, isAscending):
    for i in range(len(array)):
        if i == 0:
            continue
        if int(array[i-1]) < int(array[i]) and isAscending:
            safe = True
        elif int(array[i-1]) > int(array[i]) and not(isAscending):
            safe = True
        else:
            return False
            
        if abs(int(array[i-1]) - int(array[i])) <= 3 and abs(int(array[i-1]) - int(array[i])) >= 1:
            safe = True
        else:
            return False
    return safe

for x in f:
    array = x.split()
    
    
    if int(array[0]) < int(array[1]):
        isAscending = True
    else:
        isAscending = False
        
    safe = checkIfSafe(array, isAscending)
    
    # if its not safe
    if not(safe):
        for i in range(len(array)):
            currentArray = array.copy()
            removed = currentArray.pop(i)
            if (i == 0) or (i == 1):
                if int(currentArray[0]) < int(currentArray[1]):
                    isAscending = True
                else:
                    isAscending = False
            safe = checkIfSafe(currentArray, isAscending)
            if safe: break
            
    #print(array, " is safe: ", safe, safeAmount)
    if safe:
        safeAmount += 1
        
        

        
        
print(safeAmount)

