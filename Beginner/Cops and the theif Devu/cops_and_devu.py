for t in range(int(input())):
    m,x,y = map(int,input().split(" "))
    h = list(map(int,input().split(" ")))
    c = x*y
    count = 0
    houses = [0]*101
    for i in h:
        houses[i] = 1
        for j in range(1,c+1):
            if i-j > -1:
                houses[i-j] = 1
            if i+j < 101:
                houses[i+j] = 1
    for i in range(1,101):
        if houses[i] == 0:
            count += 1
    print(count)
