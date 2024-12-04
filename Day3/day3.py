f = open("Day3\day3.txt", "r")

mulRequirment = 0
leftNumer = ""
rightNumber = ""
result = 0

def mul(a, b):
    return int(a) * int(b)

for line in f:
    for c in line:
        if c == "m" and mulRequirment == 0:
            mulRequirment += 1
        elif c == "u" and mulRequirment == 1:
            mulRequirment += 1
        elif c == "l" and mulRequirment == 2:
            mulRequirment += 1
        elif c == "(" and mulRequirment == 3:
            mulRequirment += 1
            leftNumer = ""
        elif mulRequirment == 4 and c != ",":
            try:
                int(c)
            except ValueError:
                c = 10
            if int(c) <= 9:
                print("c: ", c, "leftunmer: ", leftNumer, " join ", leftNumer + c)
                leftNumer = leftNumer + c
            else:
                mulRequirment = 0
        elif mulRequirment == 4 and c == ",":
            mulRequirment += 1
            rightNumber = ""
        elif mulRequirment == 5 and c != ")":
            try:
                int(c)
            except ValueError:
                c = 10
            if int(c) <= 9:
                rightNumber = rightNumber + c
                print("right number is now:", rightNumber)
            else:
                mulRequirment = 0
        elif mulRequirment == 5 and c == ")":
            mulRequirment = 0
            result += mul(leftNumer, rightNumber)
            print("multiplying!", leftNumer, rightNumber)
            leftNumer = ""
            rightNumber = ""
        else:
            mulRequirment = 0
            leftNumer = ""
            rightNumber = ""
    #print("on line: ", line, " result: ", result)

print(result)
            
            