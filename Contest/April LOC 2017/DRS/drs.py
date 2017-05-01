for i in range(int(input())):
    x = []
    for j in range(int(input())):
        x.append(float(input()))
    l = [0]*6
    res = 0
    for over in x:
        rem = int(over / 80)
        l[rem] += 1
    for m in l:
        if m > 2:
            res += 2
        else:
            res += m
    print(res)
