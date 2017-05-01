for i in range(int(input())):
    n,a = map(int,input().split(" "))
    if a <= n:
        if a == 2:
            print("Ambi")
        else:
            print("Abhi")
    else:
        print("Abhi")
