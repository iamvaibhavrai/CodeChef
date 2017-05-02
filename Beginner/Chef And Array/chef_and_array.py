for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    s,p,count = 0,1,0
    for i in range(n):
        for j in range(i,n):
            s += x[j]
            p *= x[j]
            if p == s:
                count += 1
        s,p = 0,1
    print(count)
