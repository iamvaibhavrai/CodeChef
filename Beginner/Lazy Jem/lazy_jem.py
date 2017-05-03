for t in range(int(input())):
    n,b,k = map(int,input().split(" "))
    res = 0
    while(n>1):
        if n&1 == 1:
            x = (n+1)//2
            n -= x
        else:
            x = n//2
            n -= x
        res += x*k
        res += b
        k *= 2
    res += k
    print(res)
