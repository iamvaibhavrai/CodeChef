for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    y = sorted(x)
    s = set(x)
    if x == y:
        print("no")
    elif len(s) < len(x):
        print("no")
    else:
        for i in range(len(y)):
            if y[i] != i+1:
                print("no")
                break
        else:
            print("yes")
