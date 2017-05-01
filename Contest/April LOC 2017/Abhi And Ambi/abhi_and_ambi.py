for i in range(int(input())):
    n,a = map(int,input().split(" "))
    if a <= n and a%2 == 0:
        print("Ambi")
    else:
        print("Abhi")
