for t in range(int(input())):
    s = input()
    amber,brass = 0,0
    for i in s:
        if i == 'a':
            amber += 1
        else:
            brass += 1
    print(amber if amber < brass else brass)
