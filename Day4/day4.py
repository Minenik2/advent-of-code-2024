f = open("Day4\day4.txt", "r")

def checkAroundMe(c, array, i, k):
    #print(i , 0 < i < len(array), " len of array is ", len(array))
    if 0 <= i < len(array) and 0 <= k < len(array[i]):
        if array[i][k] == c:
            return True
    return False

foundOne = False
res = 0
array = []

for line in f:
    line = list(line)
    if line[len(line)-1] == "\n":
        line.remove("\n")
    array.append(line)
    
for i in range(len(array)):
    for k in range(len(array[i])):
        if array[i][k] == "A":
            #up left
            if checkAroundMe("M", array, i-1, k-1):
                if checkAroundMe("S", array, i+1, k+1):
                    if foundOne:
                        res += 1
                    else:
                        foundOne = True
            # up right
            if checkAroundMe("M", array, i-1, k+1):
                if checkAroundMe("S", array, i+1, k-1):
                    if foundOne:
                        res += 1
                    else:
                        foundOne = True
            # low left
            if checkAroundMe("M", array, i+1, k-1):
                if checkAroundMe("S", array, i-1, k+1):
                    if foundOne:
                        res += 1
                    else:
                        foundOne = True
            # low right
            if checkAroundMe("M", array, i+1, k+1):
                if checkAroundMe("S", array, i-1, k-1):
                    if foundOne:
                        res += 1
                    else:
                        foundOne = True
        foundOne = False
            
print(res)
