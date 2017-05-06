for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    smaller = float("inf")
    for i in x:
        smaller = smaller if smaller<i else i
    print(smaller*(n-1))
