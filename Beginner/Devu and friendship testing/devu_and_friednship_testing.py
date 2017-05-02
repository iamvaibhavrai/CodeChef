for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split(" ")))
    res = []
    for i in d:
        if i not in res:
            res.append(i)
    print(len(res))
