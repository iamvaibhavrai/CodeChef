for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    count = 0
    if len(x) == 1:
    for i in x:
        if i != 1 and i != 0:
            count += 1
        if count > 1:
            print("no")
            break
    else:
        print("yes")
