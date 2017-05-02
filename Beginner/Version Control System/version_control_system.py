for t in range(int(input())):
    n,m,k = map(int,input().split(" "))
    ignored = list(map(int,input().split()))
    tracked = list(map(int,input().split()))
    iandt = 0
    for i in ignored:
        if i in tracked:
            iandt += 1
    iort = len(ignored) + len(tracked) - iandt
    print(iandt,n-iort)
