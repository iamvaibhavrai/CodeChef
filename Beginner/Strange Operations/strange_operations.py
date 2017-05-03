for t in range(int(input())):
    m,k = map(int,input().split(" "))
    x = list(map(int,input().split(" ")))
    if k > 1:
        print("even")
    else:
        s = 0
        for i in x:
            s += i
        if s&1 == 0:
            print("odd")
        else:
            print("even")
