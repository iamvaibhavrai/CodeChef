for t in range(int(input())):
    n,k = map(int,input().split(" "))
    res = 0
    for i in range(n):
        time,m = map(int,input().split(" "))
        if k > time:
            k = k-time
        else:
            k = time-k
            res += k*m
            k = 0
    print(res)
