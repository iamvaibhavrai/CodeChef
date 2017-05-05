for t in range(int(input())):
    s = input()
    firstOne,zero = 0,0
    res = False
    for num in s:
        if num == '1' and firstOne == 0:
            firstOne = 1
            res = True
        if firstOne == 1 and num == '0':
            zero = 1
        if num == '1' and zero == 1:
            res = False
            break
    if res:
        print("YES")
    else:
        print("NO")
