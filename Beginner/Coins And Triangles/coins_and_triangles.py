for t in range(int(input())):
    n = int(input())
    for i in range(1,n+3):
        if (i*(i+1))//2 > n:
            print(i-1)
            break
