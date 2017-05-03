for t in range(int(input())):
    b = input()
    maximum,count = 0,0
    for i in b:
        if i == '(':
            count += 1
        else:
            count -= 1
        maximum = max(count,maximum)
    res = []
    for i in range(maximum):
        res.append('(')
    for i in range(maximum):
        res.append(')')
    print(''.join(res))
