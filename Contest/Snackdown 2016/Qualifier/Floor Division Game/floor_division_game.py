def calculateMex(l):
    mex = 0
    while True:
        if mex in l:
            mex += 1
        else:
            return mex

def calculateGrundy(n,grundy):
    if n == 0:
        return 0

    if grundy[n] != -1:
        return grundy[n]

    l = []
    l.append(calculateGrundy(n//2,grundy))
    l.append(calculateGrundy(n//3,grundy))
    l.append(calculateGrundy(n//4,grundy))
    l.append(calculateGrundy(n//5,grundy))
    l.append(calculateGrundy(n//6,grundy))

    grundy[n] = calculateMex(l)

    return grundy[n]

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        x = list(map(int,input().split(" ")))
        res = []
        for j in range(n):
            grundy = [-1]*(x[j]+1)
            res.append(calculateGrundy(x[j],grundy))
        xor = res[0]
        for j in range(1,len(res)):
            xor ^= res[j]
        if xor == 0:
            print("Derek")
        else:
            print("Henry")

if __name__ == '__main__':
    main()
