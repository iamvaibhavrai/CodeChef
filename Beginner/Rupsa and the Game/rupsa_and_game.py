for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    left,right = x[0],x[0]
    s = 0
    for i in range(1,n):
        left *= x[i]
        right *= x[i]
        s += (left+right)
        left = x[i-1]
        right = x[i]
