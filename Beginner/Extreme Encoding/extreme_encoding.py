for t in range(int(input())):
    n = int(input())
    a,b = [],[]
    for i in range(n):
        x = int(input())
        b.append(str(x>>16))
        a.append(str(x - ((x>>16)<<16)))
    print("Case {}:".format(t+1))
    print(" ".join(a))
    print(" ".join(b))
