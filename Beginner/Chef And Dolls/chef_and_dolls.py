for t in range(int(input())):
    n = int(input())
    res = 0
    for i in range(n):
        x = int(input())
        res ^= x
    print(res)
