f = open("Day4\day4.txt", "r")

def checkAroundMe(c, array, i, k):
    print(i , 0 < i < len(array), " len of array is ", len(array))
    if 0 <= i < len(array) and 0 <= k < len(array[i]):
        if array[i][k] == c:
            return True
    return False
res = 0
array = []

for line in f:
    line = list(line)
    array.append(line)
    
for i in range(len(array)):
    for k in range(len(array[i])):
        if array[i][k] == "X":
            #up left
            if checkAroundMe("M", array, i-1, k-1):
                if checkAroundMe("A", array, i-2, k-2):
                    if checkAroundMe("S", array, i-3, k-3):
                        res += 1
            # up
            if checkAroundMe("M", array, i-1, k):
                if checkAroundMe("A", array, i-2, k):
                    if checkAroundMe("S", array, i-3, k):
                        res += 1
            # up right
            if checkAroundMe("M", array, i-1, k+1):
                if checkAroundMe("A", array, i-2, k+2):
                    if checkAroundMe("S", array, i-3, k+3):
                        res += 1
            # right
            if checkAroundMe("M", array, i, k+1):
                if checkAroundMe("A", array, i, k+2):
                    if checkAroundMe("S", array, i, k+3):
                        res += 1
            # left
            if checkAroundMe("M", array, i, k-1):
                if checkAroundMe("A", array, i, k-2):
                    if checkAroundMe("S", array, i, k-3):
                        res += 1
            # low left
            if checkAroundMe("M", array, i+1, k-1):
                if checkAroundMe("A", array, i+2, k-2):
                    if checkAroundMe("S", array, i+3, k-3):
                        res += 1
            # low
            if checkAroundMe("M", array, i+1, k):
                if checkAroundMe("A", array, i+2, k):
                    if checkAroundMe("S", array, i+3, k):
                        res += 1
            # low right
            if checkAroundMe("M", array, i+1, k+1):
                if checkAroundMe("A", array, i+2, k+2):
                    if checkAroundMe("S", array, i+3, k+3):
                        res += 1
            
print(res)
