for x in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    print(sum(1 for i in range(n) if b[i] <= a[i+1] - a[i]))
