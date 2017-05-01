for i in range(int(input())):
    n,a = map(int,input().split(" "))
    if a > n and a&1 == 0:
        print("Abhi")
    else:
        print("Ambi")
