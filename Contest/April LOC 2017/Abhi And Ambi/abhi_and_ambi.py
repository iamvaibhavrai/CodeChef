res = []
def calculateMex(l):
    mex = 0
    while True:
        if mex in l:
            mex += 1
        else:
            return mex

def calculateGrundy(n):
    global res
    if n == 0:
        return 0

    l = []
    for i in range(n):
        if i+1 not in res:
            print("i",i)
            l.append(calculateGrundy(i))

    return calculateMex(l)

def main():
    t = int(input())
    global res
    for i in range(t):
        res = []
        n,a = map(int,input().split(" "))
        for j in range(n):
            res.append(calculateGrundy(a))
        xor = res[0]
        for j in range(1,len(res)):
            xor ^= res[j]
        if xor == 0:
            print("Ambi")
            print(res)
        else:
            print("Abhi")
            print(res)

if __name__ == '__main__':
    main()
