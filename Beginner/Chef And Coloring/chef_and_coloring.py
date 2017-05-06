for t in range(int(input())):
    n = int(input())
    x = input()
    r,g,b = 0,0,0
    for i in x:
        if i == 'R':
            r += 1
        if i == 'G':
            g += 1
        if i == 'B':
            b += 1
    res = r+g+b - max(r,g,b)
    print(res)
