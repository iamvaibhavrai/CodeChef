for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split(" ")))
    zeros,ones = 0,0
    for i in x:
        if i == 1:
            ones += 1
        else:
            zeros += 1
    print(zeros if zeros&1 == 1 else ones)
