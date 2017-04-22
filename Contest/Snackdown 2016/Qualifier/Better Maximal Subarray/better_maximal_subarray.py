def betterMaximalSum(a):
    tempSum = 0
    newArray = []
    maximum = 0
    countNegative = 0
    length = 0
    for i in a:
        if i < 0:
            newArray.append(tempSum)
            newArray.append(i)
            countNegative += 1
            length += 2
            tempSum = 0
        else:
            tempSum += i
        maximum  = max(maximum,i)
    if tempSum > 0:
        newArray.append(tempSum)
        length += 1

    print(newArray)

    if countNegative < len(a):
        mainSum = 0
        alternateSum = 0
        maximalSum = 0
        lastSum = 0
        for x in newArray:
            if x < 0:
                lastSum = mainSum
                mainSum += x
                if mainSum < 0:
                    mainSum = 0
                alternateSum += x
                alternateSum = alternateSum if alternateSum > lastSum else lastSum
                maximalSum = maximalSum if maximalSum > alternateSum else alternateSum
            else:
                mainSum += x
                maximalSum = maximalSum if maximalSum > mainSum else mainSum
                alternateSum += x
                maximalSum = maximalsum if maximalSum > alternateSum else alternateSum
        return maximalSum
    else:
        return maximum


def main():
    t = int(input())
    for i in range(t):
        a = list(map(int,input().split(" ")))
        print(betterMaximalSum(a))

if __name__ == '__main__':
    main()
