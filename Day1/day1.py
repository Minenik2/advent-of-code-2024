f = open("Day1\day1.txt", "r")
left = []
right = []

for x in f:
    array = x.split()
    left.append(array[0])
    right.append(array[1])

left.sort()
right.sort()

distance = 0

similarity = {}
similarityScore = 0

for i in range(len(left)):
    if left[i] not in similarity:
        similarity[left[i]] = 0
        
    distance += abs(int(left[i]) - int(right[i]))
    
for i in range(len(right)):
    if right[i] in similarity:
        similarity[right[i]] = int(similarity[right[i]]) + 1
    
for key in similarity:
    print(similarity[key])
    similarityScore += int(key) * int(similarity[key]) 

print("similarity key", distance)
print("similarity score", similarityScore)

