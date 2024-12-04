f = open("Day3\day3.txt", "r")

do = True
mulRequirment = 0
doRequirment = 0
leftNumer = ""
rightNumber = ""
result = 0

def mul(a, b):
    return int(a) * int(b)

for line in f:
    for c in line:
        if c == "d" and doRequirment == 0:
            doRequirment += 1
        elif c == "o" and doRequirment == 1:
            doRequirment += 1
        elif c == "n" and doRequirment == 2:
            doRequirment += 1
        elif c == "'" and doRequirment == 3:
            doRequirment += 1
        elif c == "t" and doRequirment == 4:
            doRequirment += 1
        elif c == "(" and doRequirment == 5:
            doRequirment += 1
        elif c == ")" and doRequirment == 6:
            do = False
        elif c == "(" and doRequirment == 2:
            doRequirment += 1
        elif c == ")" and doRequirment == 3:
            do = True
        else:
            doRequirment = 0
        
        if c == "m" and mulRequirment == 0 and do:
            mulRequirment += 1
        elif c == "u" and mulRequirment == 1 and do:
            mulRequirment += 1
        elif c == "l" and mulRequirment == 2 and do:
            mulRequirment += 1
        elif c == "(" and mulRequirment == 3 and do:
            mulRequirment += 1
            leftNumer = ""
        elif mulRequirment == 4 and c != "," and do:
            try:
                int(c)
            except ValueError:
                c = 10
            if int(c) <= 9:
                print("c: ", c, "leftunmer: ", leftNumer, " join ", leftNumer + c)
                leftNumer = leftNumer + c
            else:
                mulRequirment = 0
        elif mulRequirment == 4 and c == "," and do:
            mulRequirment += 1
            rightNumber = ""
        elif mulRequirment == 5 and c != ")" and do:
            try:
                int(c)
            except ValueError:
                c = 10
            if int(c) <= 9:
                rightNumber = rightNumber + c
                print("right number is now:", rightNumber)
            else:
                mulRequirment = 0
        elif mulRequirment == 5 and c == ")" and do:
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
            
            