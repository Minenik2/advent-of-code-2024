f = open("Day2\day2.txt", "r")

safe = False
safeAmount = 0
isAscending = False
isDecending = False

for x in f:
    array = x.split()
    
    
    if int(array[0]) < int(array[1]):
        isAscending = True
    else:
        isAscending = False
        
        
    
    for i in range(len(array)):
        if i == 0:
            continue
        # check if the array is acending or check if the array is decending
        if int(array[i - 1]) < int(array[i]) and isAscending:
            #print(array[i-1], " < ", array[i])
            safe = True
        elif int(array[i - 1]) > int(array[i]) and not(isAscending):
            safe = True
            #print(array[i-1], " > ", array[i])
        else:
            safe = False
            break
        
        if abs(int(array[i - 1]) - int(array[i])) <= 3 and abs(int(array[i - 1]) - int(array[i])) >= 1:
            safe = True
        else:
            safe = False
            #print("break", array[i - 1],"vs", array[i], " is ",  abs(int(array[i - 1]) - int(array[i])), "apart")
            break
    # if its not safe
    if not(safe):
        for i in range(len(array)):
            currentArray = array
            currentArray.pop(i)
            checkIfSafe(int(array[i - 1]), int(array[i]), isAscending)
            
    #print(array, " is safe: ", safe, safeAmount)
    if safe:
        safeAmount += 1
        
        
def checkIfSafe(a, b, isAscending):
    if int(a) < int(b) and isAscending:
        safe = True
    elif int(a) > int(b) and not(isAscending):
        safe = True
    else:
        return False
        
    if abs(int(a) - int(b)) <= 3 and abs(int(a) - int(b)) >= 1:
        return safe
    else:
        return False
        
        
print(safeAmount)

