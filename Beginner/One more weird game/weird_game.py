for t in range(int(input())):
    m,n = map(int,input().split(" "))
    count = -1
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                count += 1
            else:
                count += 2
    print(count)
