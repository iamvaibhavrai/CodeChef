for t in range(int(input())):
    n,g = map(int,input().split(" "))
    x = list(map(int,input().split(' ')))
    res = 0
    for i in x:
        d = (i // g) + 1
        if i%g > (d*g)-i:
            res += (d*g)-i
        else:
            res += i%g
    print(res)
